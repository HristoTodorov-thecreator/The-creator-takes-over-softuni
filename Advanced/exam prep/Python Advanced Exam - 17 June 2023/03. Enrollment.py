def gather_credits(credits_needed, *args):
    data = set()
    total = 0

    for name, credits in args:
        if name in data:
            continue

        if total >= credits_needed:
            break

        total += credits
        data.add(name)


    data = sorted(data)

    if total >= credits_needed:
        result = f'Enrollment finished! Maximum credits: {total}.\nCourses: {", ".join(data)}'
        return result
    else:
        output = f"You need to enroll in more courses! You have to gather {credits_needed - total} credits more."
        return output



