__author__ = 'qhuydtvt'

from datetime import datetime

from versions import Version
from questions import Question
from question_packs import QuestionPack
from app import remove_dollar_sign

from answer_choices import AnswerChoice
import re


import xlrd

host = "ds011840.mlab.com"
port = 11840
db_name = "gmat"
user_name = "admin"
password = "admin"

#from questions import Question, QuestionCollection
#import mongoengine

#db = mongoengine.connect("gmat", host='103.1.209.92', port=27017)
#
# question_list = [question for question in Question.objects]
#
# version = "0.0.1"
#
# question_collection = QuestionCollection.objects[0]
# print(question_collection.to_json())

# db.close()

from question_packs import QuestionPack, QuestionPackCollection
from questions import QuestionCollection, Question
from question_packs import QuestionPack

import mongoengine



# question_collection = QuestionCollection.objects[0]
# questions = question_collection.questions


# for question in questions:
#     print(question.to_json())
#     q = Question(
#         type = question.type,
#         sub_type = question.sub_type,
#         stimulus = question.stimulus,
#         stem = question.stem,
#         answer_choices = question.answer_choices,
#         right_answer = question.right_answer,
#         explanation = question.explanation
#     )
#     q.save()
#
# questions = Question.objects

# for question in questions:
#     print(question.to_json())

# v = Version(value="0.0.1")
# v.save()


import xlrd

def test():
    INFO_SHEET_IDX = 0
    QUESTION_STEP = 5

    wb = xlrd.open_workbook("SC 1 - 10 - Commented.xlsx")

    sheet = wb.sheet_by_index(INFO_SHEET_IDX)

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

def load_data_from_excel(excel_path):
    INFO_SHEET_IDX = 0
    QUESTION_ROW_STEP = 5
    STIMULUS_COL = 1
    STEM_COL = 2
    ANSWERS_COL = 3
    RIGHT_ANSWER_COL = 4
    EXPLANATION_COL = 5
    NOTE_COL = 6
    TYPE_COL = 7
    SUB_TYPE_COL = 8

    wb = xlrd.open_workbook(excel_path)

    sheet = wb.sheet_by_index(INFO_SHEET_IDX)

    questions = []

    for row_index in range(1, sheet.nrows, QUESTION_ROW_STEP):
        print("row_index", row_index)
        stimulus = sheet.cell(row_index, STIMULUS_COL).value
        if not stimulus or stimulus == "":
            print("Error at row: ", row_index)
            return None
        stem = sheet.cell(row_index, STEM_COL).value
        answer_choices = []
        for r_idx in range(row_index, row_index + QUESTION_ROW_STEP - 1):
            ans_choice = sheet.cell(r_idx, ANSWERS_COL).value
            explanation = sheet.cell(r_idx, EXPLANATION_COL).value
            note = sheet.cell(r_idx, NOTE_COL).value
            answer_choices.append({"choice": ans_choice,
                            "explanation": explanation,
                            "note": note})

        right_answer = sheet.cell(row_index, RIGHT_ANSWER_COL).value
        # answer_choices = [
        #     sheet.cell(row_index, ANSWERS_COL),
        #     sheet.cell(row_index + 1, ANSWERS_COL),
        #     sheet.cell(row_index + 2, ANSWERS_COL),
        #     sheet.cell(row_index + 3, ANSWERS_COL),
        #     sheet.cell(row_index + 4, ANSWERS_COL)
        # ]
        # explanations = [
        #     sheet.cell(row_index, EXPLANATION_COL),
        #     sheet.cell(row_index + 1, EXPLANATION_COL),
        #     sheet.cell(row_index + 2, EXPLANATION_COL),
        #     sheet.cell(row_index + 3, EXPLANATION_COL),
        #     sheet.cell(row_index + 4, EXPLANATION_COL)
        # ]
        #
        # notes = [
        #     sheet.cell(row_index, NOTE_COL),
        #     sheet.cell(row_index + 1, NOTE_COL),
        #     sheet.cell(row_index + 2, NOTE_COL),
        #     sheet.cell(row_index + 3, NOTE_COL),
        #     sheet.cell(row_index + 4, NOTE_COL)
        # ]
        type = sheet.cell(row_index, TYPE_COL)
        sub_type = sheet.cell(row_index, SUB_TYPE_COL)

        questions.append(
            {
                "type" : type,
                "sub_type": sub_type,
                "stimulus": stimulus,
                "stem": stem,
                "answer_choices":answer_choices,
                "right_answer" : right_answer
            }
        )
        # Question(
        #     type=type,
        #     sub_type=sub_type,
        #     stimulus=stimulus,
        #     stem=stem,
        #     answer_choices=answer_choices,
        #     right_answer= right_answer
        #
    return questions

def load_objects_from_excel(excel_path):
    INFO_SHEET_IDX = 0
    QUESTION_ROW_STEP = 5
    STIMULUS_COL = 1
    STEM_COL = 2
    ANSWERS_COL = 3
    RIGHT_ANSWER_COL = 4
    EXPLANATION_COL = 5
    NOTE_COL = 6
    TYPE_COL = 7
    SUB_TYPE_COL = 8

    wb = xlrd.open_workbook(excel_path)

    sheet = wb.sheet_by_index(INFO_SHEET_IDX)

    questions = []

    answer_map = {
        "a" : 0,
        "b" : 1,
        "c" : 2,
        "d" : 3,
        "e" : 4,
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "D" : 3,
        "E" : 4
    }

    label_map2 = ["A", "B", "C", "D", "E"]

    for row_index in range(1, sheet.nrows, QUESTION_ROW_STEP):
        print("row_index", row_index)
        stimulus = sheet.cell(row_index, STIMULUS_COL).value
        if not stimulus or stimulus == "":
            print("Error at row: ", row_index)
            return None
        stem = sheet.cell(row_index, STEM_COL).value
        answer_choices = []
        ans_idx = 0
        for r_idx in range(row_index, row_index + QUESTION_ROW_STEP - 1):
            ans_choice = str(sheet.cell(r_idx, ANSWERS_COL).value).strip()
            # print(re.sub("^[a-eA-E].", "", ans_choice).strip())
            explanation = sheet.cell(r_idx, EXPLANATION_COL).value
            note = sheet.cell(r_idx, NOTE_COL).value
            answer_choices.append(
                AnswerChoice(
                    index=ans_idx,
                    choice=re.sub("^[a-eA-E].", "", ans_choice).strip(),
                    explanation=re.sub("^[a-eA-E].", "", explanation).strip(),
                    note=re.sub("^[a-eA-E].", "", note).strip()
                ))
            ans_idx+=1

        right_answer = answer_map[str(sheet.cell(row_index, RIGHT_ANSWER_COL).value).strip()]
        type = sheet.cell(row_index, TYPE_COL).value
        sub_type = sheet.cell(row_index, SUB_TYPE_COL).value

        questions.append(
            Question(
                type=type,
                sub_type=sub_type,
                stimulus=stimulus,
                stem=stem,
                answer_choices=answer_choices,
                right_answer=right_answer,
            )
        )
        # Question(
        #     type=type,
        #     sub_type=sub_type,
        #     stimulus=stimulus,
        #     stem=stem,
        #     answer_choices=answer_choices,
        #     right_answer= right_answer
        #
    return questions

# questions = Question.objects
#
# question_pack = QuestionPack(available_time="2016-03-14",
#                              question_ids = [str(question.id) for question in questions ])
# version = Version.objects[0]
# question_collection = QuestionCollection(version=version.value, questions=[q for q in questions])
# remove_dollar_sign(str(question_collection.to_json()))
# question_pack.save()

# print(question_pack.to_json())

# question_pack.save()



# def get_gmat_question_collection():
#     questions = Question.objects
#     version = Version.objects[0]
#     question_collection = QuestionCollection(version=version.value, questions=questions)
#     return remove_dollar_sign(str(question_collection.to_json()))
#     #return questions
#
# get_gmat_question_collection()

# db.close()

def load_questions_for_pack1():
    for data in load_objects_from_excel("SC 1 - 10 - Commented.xlsx"):
        data.save()

def load_question_pack1():
    questions = Question.objects
    q_p = QuestionPack(
        available_time="2016-03-26",
        question_ids=[str(question.id) for question in questions]
    )
    q_p.save()


if __name__ == "__main__":

    db = mongoengine.connect(db_name,
        host=host, port=port, username=user_name, password=password)

    # print(load_data_from_excel("SC 1 - 10 - Commented.xlsx"))
    # i = 0
    # for data in load_data_from_excel("SC 1 - 10 - Commented.xlsx"):
    #     if i == 5:
    #         print("stimulus", data['stimulus'])
    #         print("stem", data['stem'])
    #         for ans in data['answer_choices']:
    #             print("------------------------------------------------------------")
    #             print(ans['choice'])
    #             print(ans['explanation'])
    #             print(ans['note'])
    #     i += 1
    # pass
    load_questions_for_pack1()
    load_question_pack1()
    db.close()