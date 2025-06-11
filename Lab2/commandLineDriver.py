import requests

def maindriver():

    url = "http://127.0.0.1:8080/"

    loop = True
    while loop:
        print("1. FastAPI routes")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            print("FastAPI routes:")
            print("1. root_route")
            print("2. time_route")
            print("3. animal_route")
            print("4. color_route")
            print("5. collegePost_route")
            print("6. query_route")
            print("7. carPost_route")
            print("8. sportsQuery_route")
            print("9. bookQuery_route")
            print("10. hometownQuery_route")
            print("11. headers")
            print("12. cookies")
            choice1 = input("Enter your choice: ")

            if choice1 == '1':
                print(requests.get(f"{url}").json())
            elif choice1 == '2':
                print(requests.get(f"{url}time").json())
            elif choice1 == '3':
                animal = input("Enter animal name: ")
                print(requests.get(f"{url}animal/{animal}").json())
            elif choice1 == '4':
                color = input("Enter color name: ")
                print(requests.get(f"{url}color/{color}").json())
            elif choice1 == '5':
                CollegeStudentInput = {
                    "name": input("Enter name: "),
                    "age": int(input("Enter age: ")),
                    "year": int(input("Enter year: ")),
                    "major": input("Enter major: ")
                }
                print(requests.post(f"{url}college-student", json=CollegeStudentInput).json())
            elif choice1 == '6':
                name_age_country = {
                    "name": input("Enter name: "),
                    "age": input("Enter age: "),
                    "country": input("Enter country: ")
                }
                print(requests.get(f"{url}query", params=name_age_country).json())
            elif choice1 == '7':
                CarMakeModel = {
                    "make": input("Enter make: "),
                    "model": int(input("Enter model: ")),
                    "year": int(input("Enter year: "))
                }
                print(requests.post(f"{url}car", json=CarMakeModel).json())
            elif choice1 == '8':
                sport = input("Enter sport name: ")
                print(requests.get(f"{url}sports", params={"name": sport}).json())
            elif choice1 == '9':
                genre = input("Enter genre: ")
                book = input("Enter book name: ")
                print(requests.get(f"{url}book", params={"genre": genre, "book": book}).json())
            elif choice1 == '10':
                highschool = input("Enter high school: ")
                town = input("Enter town: ")
                print(requests.get(f"{url}hometown", params={"highschool": highschool, "town": town}).json())
            #not working
            elif choice1 == '11':
                headers = {
                    "Content-Type": "application/json",
                    "X-Custom-header": "CustomValue",
                    "user_email": "ColeF",
                    "my-val": "my_value"
                }
                print(requests.get(f"{url}headers", headers=headers).json())
            #not working
            elif choice1 == '12':
                cookies = {"username": "test_user"}
                print(requests.get(f"{url}read_cookie", cookies=cookies).json())
            else:
                print("Invalid choice")
        elif choice == '2':
            print("Exiting")
            loop = False

if __name__ == '__main__':
    maindriver()