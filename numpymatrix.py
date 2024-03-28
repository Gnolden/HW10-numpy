import numpy as np


# student names
def generate_student_names(num_students):
    georgian_first_names = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ', 'კლარა', 'სიმონ',
                            'ანზორ', 'სოფია', 'სოსო', 'ნელი', 'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია',
                            'ემა', 'იზოლდა', 'ომარ', 'ტატიანა', 'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან',
                            'სიმონ', 'ნელი', 'ბადრი', 'მადონა', 'ირინე', 'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა',
                            'როინ', 'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა', 'გოჩა', 'მურმან']
    georgian_last_names = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი', 'ბუჩუკური',
                           'ტყებუჩავა', 'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა',
                           'ნაკაშიძე', 'ღურწკაია', 'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია',
                           'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე', 'ხარაბაძე', 'მუსაევა', 'მამულაშვილი',
                           'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა', 'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე',
                           'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე',
                           'ინასარიძე', 'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი']

    student_names = []
    for _ in range(num_students):
        first_name = np.random.choice(georgian_first_names)
        last_name = np.random.choice(georgian_last_names)
        student_names.append(f"{first_name} {last_name}")
    return student_names


# random scores
def generate_scores(num_students, num_subjects):
    return np.random.randint(1, 101, size=(num_students, num_subjects))


num_students = 100
student_names = generate_student_names(num_students)
subjects = ['ქართული', 'მათემატიკა', 'ინგლისური', 'ისტორია', 'ფიზიკა']
scores = generate_scores(num_students, len(subjects))

table = np.column_stack((student_names, scores))
print("Generated table:")
print(
    "----------------------------------------------------------------------------------------------------------------------------")
print("| {:<20} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |".format("Student Name", "ქართული", "მათემატიკა",
                                                                       "ინგლისური", "ისტორია", "ფიზიკა"))
print(
    "----------------------------------------------------------------------------------------------------------------------------")
for row in table:
    print("| {:<20} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |".format(*row))
print(
    "----------------------------------------------------------------------------------------------------------------------------")

average_scores = np.mean(scores, axis=1)
highest_avg_index = np.argmax(average_scores)
print("\nყველაზე მაღალი საშუალო ქულის მქონე სტუდენტი:", student_names[highest_avg_index], "საშუალო ქულით",
      average_scores[highest_avg_index])

math_scores = scores[:, subjects.index('მათემატიკა')]
highest_math_score_index = np.argmax(math_scores)
lowest_math_score_index = np.argmin(math_scores)
print("\nსტუდენტი მათემატიკაში ყველაზე მაღალი ქულით:", student_names[highest_math_score_index], "ქულა:",
      math_scores[highest_math_score_index])
print("სტუდენტი მათემატიკაში ყველაზე დაბალი ქულით:", student_names[lowest_math_score_index], "ქულა:",
      math_scores[lowest_math_score_index])

english_scores = scores[:, subjects.index('ინგლისური')]
average_english_score = np.mean(english_scores)
print("\nყველა სტუდენტი რომლის ინგლისურის ქულაც მეტია საშუალო ინგლისურის ქულაზე:")
for i, name in enumerate(student_names):
    if english_scores[i] > average_english_score:
        print(name)
