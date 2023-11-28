import pandas as pd

df = pd.read_csv('kookmin_univ.csv',encoding='CP949')
univs = ["글로벌인문,지역대학", "사회과학대학", "법과대학", "경상대학", "창의공과대학", "조형대학", "과학기술대학", "예술대학", "경영대학", "소프트웨어융합대학", "건축대학", "자동차융합대학"]

while True:
    # 단과대 입력, 단과대에 속한 학과들 보여주기.
    print("=== 단과대입니다 ===")
    num = -1
    for i in univs:
        num += 1
        print(num, i)

    print()
    univ = input('단과대를 입력해주세요 ---> ')
    print()

    if univ in univs:
        while True:
            print("=== 해당 단과대에 속한 학과들입니다 ===")
            print(df.loc[df["단과대"] == univ, ["학과"]])
            print()
            subject_list = df.loc[df["단과대"] == univ, "학과"].tolist()

            subject = input('학과를 입력해주세요 ---> ')
            print(f"입력받은 학과: {subject}")
            # 학과 입력, 입력받은 학과의 열람하고 싶은 Option지 보여주기
            if subject in subject_list:

                graduate = int(df.loc[df["학과"] == subject, ["졸업이수학점"]].values[0].item())

                # 교양
                main = int(df.loc[df["학과"] == subject, ["핵심교양학점"]].values[0].item())
                basic = int(df.loc[df["학과"] == subject, ["기초교양학점"]].values[0].item())
                free = int(df.loc[df["학과"] == subject, ["자유교양학점"]].values[0].item())
                # 전공
                major = int(df.loc[df["학과"] == subject, ["전공학점"]].values[0].item())
                # 일반선택 (교양 초과학점 발생 시 일반선택에서 빠짐.)
                normal = int(df.loc[df["학과"] == subject, ["일반선택학점"]].values[0].item())

                print()
                print("=== 해당 학과의 졸업하기 위한 학점입니다. ===")
                print(f"핵심교양학점 : {main}학점\n* 인문I, 인문II, 소통, 글로벌, 창의 -> 3학점씩 수강해야 합니다.")
                print(f"기초교양학점 : {basic}학점")
                print(f"핵심교양학점 : {free}학점")
                print(f"핵심교양학점 : {major}학점")
                print(f"핵심교양학점 : {normal}학점")
                print()

                # 인문I, 인문II, 소통, 글로벌, 창의
                now_main = list(map(int,input("지금까지 들은 핵심교양학점은 몇 학점입니까? \n(인문I, 인문II, 소통, 글로벌, 창의 띄어쓰기 구분하여 입력) --> ").split()))
        
                now_basic = int(input("지금까지 들은 기초교양학점은 몇 학점입니까? --> "))
                now_free = int(input("지금까지 들은 자유교양학점은 몇 학점입니까? --> "))

                now_major = int(input("지금까지 들은 전공학점은 몇 학점입니까? --> "))
                now_normal = int(input("지금까지 들은 일반선택학점은 몇 학점입니까? --> "))

            
                while True:
                    print()
                    print('=== 열람하고 싶은 Option을 선택해주세요 ===')
                    print('1. 졸업이수학점')
                    print('7. 가능한연계전공 및 연계전공학점')
                    print('8. 가능한융합전공 및 융합전공학점')
                    print('9. 부전공학점')
                    print('0. 학과 다시 선택하기')
                    option = int(input("숫자로 입력해주세요 ---> "))
                    print()

                    if option == 1:
                        graduate = int(df.loc[df["학과"] == subject, ["졸업이수학점"]].values[0].item())
                        move_now_normal = 0

                        # 교양 초과학점 발생시 일반선택 학점으로 넘겨줘야 함.
                        # 단 들을 수 있는 교양 학점은 정해져 있음. (50학점)
                        limit_cul = 50

                        main_sum = 0
                        for i in range(5):
                            if (main//5 - now_main[i] < 0):
                                move_now_normal += now_main[i] - main//5
                                now_main[i] = main//5
                            main_sum += now_main[i]

                        if (basic - now_basic < 0) or (free - now_free < 0):
                            if (basic - now_basic < 0):
                                move_now_normal += now_basic - basic
                                now_basic = basic
                            if (free - now_free < 0):
                                move_now_normal += now_free - free
                                now_free = free

                        # 단 들을 수 있는 교양 학점은 정해져 있음. (50학점)
                        if move_now_normal + main_sum + now_basic + now_free > limit_cul:
                            move_now_normal = (limit_cul - (main_sum + now_basic + now_free))

                        # 인문I, 인문II, 소통, 글로벌, 창의
                        main_list = ['인문I', '인문II', '소통', '글로벌', '창의']
                        tmp = -1
                        for i in range(5):
                            if main//5 - now_main[i] > 0:
                                print(f"!!! 졸업하기까지 들어야 할 핵심교양 중 '{main_list[i]}'이 {main//5 - now_main[i]}학점 남아있습니다 !!!")

                        if (basic - now_basic > 0):
                            print(f"!!! 졸업하기까지 들어야 할 기초교양이 {basic - now_basic}학점 남아있습니다 !!!")
                        if (free - now_free > 0):
                            print(f"!!! 졸업하기까지 들어야 할 자유교양이 {free - now_free}학점 남아있습니다 !!!")
                        if (major - now_major > 0):
                            print(f"!!! 졸업하기까지 들어야 할 전공이 {major - now_major}학점 남아있습니다 !!!")
                        if (normal - now_normal - move_now_normal > 0):
                            print(f"!!! 졸업하기까지 들어야 할 일반선택이 {normal - now_normal - move_now_normal}학점 남아있습니다 !!!")
                        
                        print()
                        print(f"{subject}학생이 졸업하기까지 들어야 할 학점은 {graduate - (main_sum + now_basic + now_free + now_major + now_normal + move_now_normal)}입니다.")

                
                    # 다전공 선택사항
                    elif option == 7:
                        link_major = df.loc[df["학과"] == subject, ["연계전공"]].values[0].item()
                        link_grade = df.loc[df["학과"] == subject, ["연계전공다전공이수학점"]].values[0].item()
                        if str(link_major) == "nan" or str(link_grade) == "nan":
                            print("해당 전공으로는 연계전공이 불가합니다.")
                        else:
                            # 여러개 있을 경우 처리해줘야 함.
                            print(subject, str(link_major), int(link_grade))
                       
                    elif option == 8:
                        mix_major = df.loc[df["학과"] == subject, ["융합전공"]].values[0].item()
                        mix_grade = int(df.loc[df["학과"] == subject, ["융합전공다전공이수학점"]].values[0].item())
                        
                        if str(mix_major) == "nan" or str(mix_grade) == "nan":
                            print("해당 전공으로는 융합전공이 불가합니다.")
                        else:
                            # 여러개 있을 경우 처리해줘야 함.
                            print(subject, str(mix_major), str(mix_grade))

                # 부전공 선택사항
                    elif option == 9:
                        sub = int(df.loc[df["학과"] == subject, ["부전공"]].values[0].item())
                        now_sub = int(input("지금까지 들은 일반선택학점은 몇 학점입니까? --> "))
                        print(f"{subject}학생이 졸업하기까지 들어야 할 일반선택학점은 {sub - now_sub}입니다.")

                    elif option == 0:
                        break

                    else:
                        print("올바른 번호를 입력해주세요.")
                

            else:
                print(f"{subject}는 등록된 학과가 아닙니다. 다시 입력해주세요.")
                continue
    else:
        print(f"{univ}는 등록된 단과대가 아닙니다. 다시 입력해주세요.")
        continue

# calculator