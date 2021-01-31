def highFive(items):
    student = {}
    for sid, score in items:
        if sid in student:
            student[sid].append(score)
        else:
            student[sid] = [score]
    print(student)

    def calculate_average(x):
        x = sorted(x, reverse=True)
        return int(sum(x[:5])/5)


    output = []
    for i in student:
        output.append([i,calculate_average(student[i])])
        print(output)
    return sorted(output)

if __name__ == "__main__":
	print(highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
