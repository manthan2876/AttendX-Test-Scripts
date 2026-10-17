# AttendX attendance automation test

def test_attendance():
    student_id = "STU101"
    attendance_status = "Present"

    assert student_id != ""
    assert attendance_status in ["Present", "Absent"]

    print("Attendance test passed")


if __name__ == "__main__":
    test_attendance()
