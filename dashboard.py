import functions

def dashboard():
    print("ENTER 1 TO GET THE SEX RATIO")
    print("ENTER 2 TO GET THE HIGHEST MARKS ACROSS ALL SUBJECTS")
    print("ENTER 3 TO GET THE NO. OF STUDENTS WHO SCORED MORE THAN THE CUTOFF(200)")
    print("ENTER 4 TO GET THE AVERAGE SCORES OF MALE AND FEMALE STUDENTS")
    print("ENTER 5 TO GET THE HIGHEST AND LOWEST SCORES BY A STUDENT ")
    print("ENTER 6 TO GET THE TABULAR DISPLAY OF AVERAGE SCORES BY MALE AND FEMALE")

    inp=int(input())

    if inp==1:
        functions.sexratio()
    elif inp==2:
        functions.highestmarks()
    elif inp==3:
        functions.studentspassed()
    elif inp==4:
        functions.avg_male_female()
    elif inp==5:
        functions.highestlowestscore()
    elif inp==6:
        functions.avg_male_female()


