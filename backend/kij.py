courses = [
    ['كوب حراري', 50],
    ['كوب زجاجي', 45],
    ['كوب خشبي', 40],
    ['كوب ستانلس ستيل', 30]
]
while True:
    print("\nاختر رقم المنتج:")

    for number, course_item in enumerate(courses, start=1):
        print(f"{number}. {course_item[0]} - السعر: {course_item[1]} ريال")

    user_input = input("اكتب الرقم (أو اكتب 'خروج' لإنهاء الموقع): ")

    if user_input.lower() == "خروج":
        print("تم إنهاء الموقع. شكرًا لك!")
        break
    if user_input.isdigit():
        selected = int(user_input)
        if 1 <= selected <= len(courses):
            course_name, course_price = courses[selected - 1]
            total_price = course_price * 1.15  # الضريبة 15%
            print(f"السعر شامل الضريبة الكوب '{course_name}' هو: {total_price:.2f} ريال")
        else:
            print(f"الرقم غير صحيح! اختر رقمًا بين 1 و {len(courses)}")
    else:
        print("يرجى إدخال رقم صالح")