#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Simple Student Management System
student_name=input("Student name:")
student_surname=input("Student surname:")


# In[8]:


i=0
while i<3:
    Check_name = input("Enter student name : ")
    Check_surname = input("Enter student surname : ")

    if (Check_name == student_name and Check_surname==student_surname):
        print("Welcome:", student_name , student_surname)
        break
    else:
        print("Please Try Again!")
        i+=1
    if(i==3):
        print("failed")


# In[9]:


courses=[]
for i in range(5):
    item=input("Course name:")
    courses.append(item)
print(courses)


# 

# In[13]:


student_courses=[]
j=int(input("How many lesson will you choose:"))
if j<3 or j>5:
    print("You failed in class.")
else:
    for i in range(j):
        student_courses=input("choose courses:")


# In[14]:


exam_course=input("Exam couse:")


# In[15]:


exam_grades={'midterm':88,'final':95,'project':55}


# In[17]:


course_note=((exam_grades['midterm']*30)/100)+((exam_grades['final']*50)/100)+((exam_grades['project']*20)/100)
note=''


# In[18]:


if course_note>90:
    note='AA'
elif course_note>70 and course_note<90:
    note='BB'
elif course_note>50 and course_note<70:
    note='CC'
elif course_note>30 and course_note<50:
    note='DD'
elif course_note<30:
    note='FF'
    print("Failed Course")


# In[19]:


print(note)


# In[ ]:




