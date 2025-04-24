from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception:
            raise Exception("Software cannot be installed")

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception:
            raise Exception("Software cannot be installed")

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = next(h for h in System._hardware if h.name == hardware_name)
            software = next(s for s in System._software if s.name == software_name)
            hardware.uninstall(software)
            System._software.remove(software)
            return None
        except StopIteration:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_memory = sum(h.memory for h in System._hardware)
        total_used_memory = sum(s.memory_consumption for s in System._software)
        total_capacity = sum(h.capacity for h in System._hardware)
        total_used_space = sum(s.capacity_consumption for s in System._software)

        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {total_used_space} / {total_capacity}"

    @staticmethod
    def system_split():
        result = []
        for h in System._hardware:
            express = [s for s in h.software_components if s.software_type == "Express"]
            light = [s for s in h.software_components if s.software_type == "Light"]
            mem_used = sum(s.memory_consumption for s in h.software_components)
            cap_used = sum(s.capacity_consumption for s in h.software_components)
            components = ', '.join(s.name for s in h.software_components) or "None"

            result.append(
                f"Hardware Component - {h.name}\n"
                f"Express Software Components: {len(express)}\n"
                f"Light Software Components: {len(light)}\n"
                f"Memory Usage: {mem_used} / {h.memory}\n"
                f"Capacity Usage: {cap_used} / {h.capacity}\n"
                f"Type: {h.hardware_type}\n"
                f"Software Components: {components}"
            )
        return "\n".join(result)