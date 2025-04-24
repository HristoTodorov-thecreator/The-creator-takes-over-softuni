from sys import maxsize


jobs = [int(job) for job in input().split(', ')]
index = int(input())
total = 0
current_index = -maxsize

while current_index != index:
    current_index = jobs.index(min(jobs))  # the first index from min
    current_job = min(jobs)  # take the min from jobs
    jobs[current_index] = max(jobs) + 1  # make it max to not use it again
    total += current_job  # add it to the total
print(total)