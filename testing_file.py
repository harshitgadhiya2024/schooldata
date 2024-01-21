import random
import json
from constant import constant_data

classes = ["A", "B", "C", "D"]
department = ["Standard-7", "Standard-8", "Standard-9", "Standard-10", "11-science","12-science","11-commerce","12-arts","12-commerce",
              "11-arts"]
gender = ["Male", "Female"]
qualification = ["MBA", "BE", "ME", "BCA","MCA"]
mapping_dict = constant_data.get("city_province_mapping", {})
all_city_list = list(mapping_dict.keys())

li_data_main = []
for var in range(10,100):
    student_dict = {
        "photo_link": "static/assets/img/profiles/avatar-01.jpg",
        "student_id": "899159766511",
        "username": "harshitpatel",
        "first_name": "harshit",
        "last_name": "gadhiya",
        "password": "Har@#0401",
        "dob": "18-01-2024",
        "gender": "Male",
        "contact_no": "+31 9348343848",
        "emergency_contact_no": "+31 9343834984",
        "email": "a@gmail.com",
        "address": "ahmedabad",
        "city": "Almelo",
        "province": "Overijssel",
        "admission_date": "18-01-2024",
        "classes": "B",
        "department": "Standard-8",
        "batch_year": "2020",
        "type": "student",
        "inserted_on": "01-18-2024 20:20:37",
        "updated_on": "01-18-2024 20:20:37"
    }
    try:
        student_id = int(student_dict["student_id"])
        student_dict["student_id"] = str(student_id+var)
    except:
        pass

    student_dict["username"] = student_dict["username"]+str(var)
    student_dict["email"] = student_dict["email"].split("@")[0]+str(var)+"@"+student_dict["email"].split("@")[-1]
    student_dict["classes"] = random.choice(classes)
    student_dict["department"] = random.choice(department)
    student_dict["city"] = random.choice(all_city_list)
    student_dict["gender"] = random.choice(gender)
    student_dict["province"] = mapping_dict.get(student_dict["city"], "")
    li_data_main.append(student_dict)

print(li_data_main)

with open('student_data.json', 'w') as json_file:
    json.dump(li_data_main, json_file)

li_data_main1 = []
for var1 in range(10,15):
    admin_dict = {
      "photo_link": "static/assets/img/profiles/avatar-01.jpg",
      "admin_id": "1805151180663192",
      "username": "jaypatel8980",
      "first_name": "jay",
      "last_name": "gadhiya",
      "password": "Har@#0401",
      "gender": "Male",
      "contact_no": "+31 9237973298",
      "emergency_contact_no": "+31 9837937987",
      "email": "hgadhiya@gmail.com",
      "address": "ahemdabad",
      "city": "Amersfoort",
      "province": "Utrecht",
      "type": "admin",
      "inserted_on": "01-21-2024 00:47:48",
      "updated_on": "01-21-2024 00:47:48"
    }
    try:
        admin_id = int(admin_dict["admin_id"])
        admin_dict["admin_id"] = str(admin_id+var1)
    except:
        pass

    admin_dict["username"] = admin_dict["username"]+str(var1)
    admin_dict["email"] = admin_dict["email"].split("@")[0]+str(var1)+"@"+admin_dict["email"].split("@")[-1]
    admin_dict["city"] = random.choice(all_city_list)
    admin_dict["gender"] = random.choice(gender)
    admin_dict["province"] = mapping_dict.get(admin_dict["city"], "")
    li_data_main1.append(admin_dict)

print(li_data_main1)

with open('admin_data.json', 'w') as json_file:
    json.dump(li_data_main1, json_file)

li_data_main2 = []
for var2 in range(10,100):
    teacher_dict = {
      "photo_link": "static/uploads/profiles/teacher_teacher01.jpg",
      "teacher_id": "26580104304686",
      "username": "teacher01",
      "first_name": "teacher",
      "last_name": "teacher",
      "password": "Har@#0401",
      "dob": "21-01-2024",
      "gender": "Male",
      "contact_no": "+31 9237892788",
      "emergency_contact_no": "+31 8983279832",
      "email": "hgassdhiya@gmail.com",
      "address": "netherlands",
      "city": "Almere",
      "province": "Flevoland",
      "qualification": "MCA",
      "department": "Standard-10",
      "subject": "Gujarati",
      "joining_date": "21-01-2024",
      "type": "teacher",
      "inserted_on": "01-21-2024 04:17:00",
      "updated_on": "01-21-2024 04:17:00"
    }
    try:
        teacher_id = int(teacher_dict["teacher_id"])
        teacher_dict["teacher_id"] = str(teacher_id+var2)
    except:
        pass

    teacher_dict["username"] = teacher_dict["username"]+str(var2)
    teacher_dict["email"] = teacher_dict["email"].split("@")[0]+str(var2)+"@"+teacher_dict["email"].split("@")[-1]
    teacher_dict["department"] = random.choice(department)
    teacher_dict["subject"] = random.choice(["English", "Hindi","Gujarati","Maths","Science","Social Science"])
    teacher_dict["qualification"] = random.choice(qualification)
    teacher_dict["city"] = random.choice(all_city_list)
    teacher_dict["gender"] = random.choice(gender)
    teacher_dict["province"] = mapping_dict.get(teacher_dict["city"], "")
    li_data_main2.append(teacher_dict)

print(li_data_main2)

with open('teacher_data.json', 'w') as json_file:
    json.dump(li_data_main2, json_file)