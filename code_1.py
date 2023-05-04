total = 0;
counter = 1;
while counter <= 10:
    grade = int(input("점수 입력하세요: "));
    total = grade + total;
    counter = counter + 1;
average = total / 10;10
print("평균 :", average);