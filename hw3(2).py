# start    answer 2    elif

grade: int = int(input("enter your grade:"))

if grade >= 0 and grade <= 40:
    print("try harder next time")
elif grade >= 41 and grade <= 60:
    print("you getting there, need some more work")
elif grade >= 61 and grade <= 80:
    print("pretty good")
elif grade >= 81 and grade <= 95:
    print("awesome!")
elif grade >= 96 and grade <= 100:
    print("exellent!! you are a star")
else:
    print("illegal grade")

# end

#start answer 2 match_case

grade: int = int(input("enter your grade:"))

match grade:
    case grade [0-40]: # i don't know how to do range in match case
        print("try harder next time")



