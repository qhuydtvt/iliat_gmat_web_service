__author__ = 'qhuydtvt'

import xlrd


INFO_SHEET_IDX = 0
QUESTION_STEP = 5

wb = xlrd.open_workbook("SC 1 - 10.xlsx")

sheet = wb.sheet_by_index(INFO_SHEET_IDX)

print(sheet.nrows)
questions = []
for row_index in range(1, sheet.nrows, QUESTION_STEP):
    stimulus = sheet.cell(row_index, 1)
    answers = [
        sheet.cell(row_index, 3),
        sheet.cell(row_index + 1, 3),
        sheet.cell(row_index + 2, 3),
        sheet.cell(row_index + 3, 3),
        sheet.cell(row_index + 4, 3)
    ]
    right_answer = sheet.cell(row_index, 4)
    explanations = [
        sheet.cell(row_index, 5),
        sheet.cell(row_index + 1, 5),
        sheet.cell(row_index + 2, 5),
        sheet.cell(row_index + 3, 5),
        sheet.cell(row_index + 4, 5)
    ]

    notes = [
        sheet.cell(row_index, 6),
        sheet.cell(row_index + 1, 6),
        sheet.cell(row_index + 2, 6),
        sheet.cell(row_index + 3, 6),
        sheet.cell(row_index + 4, 6)
    ]
    type = sheet.cell(row_index, 7)
    type = sheet.cell(row_index, 8)

    questions.append(
        {
            "stimulus": stimulus,
            "answers": answers,
            "right_answer": right_answer,
            "explanations": explanations,
            "notes": notes,
            "type": type
        }
    )

for question in questions:

    print("####stimulus######")
    print(question["stimulus"])

    print("####Answers######")
    for a in question["answers"]:
        print(a)

    print("####explanations######")
    for e in question["explanations"]:
        print(e)

    print("####Note######")
    for note in (question["notes"]):
        print(note)

    print("####Type######")
    print(question["type"])

    print("------------------------------------------------------------")
