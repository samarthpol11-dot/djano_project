# Create data for your mock exam

1. Run migrations and create a superuser (see README).
2. Sign in at `/admin/`.
3. Add a Course, then a Lesson for that course.
4. Add a Question for the lesson and at least two Choices.
5. Mark exactly one Choice as correct.
6. Create a normal user at `/admin/auth/user/` or register one through Django admin.
7. Sign in as that user in the browser, open the course, and select **Take mock exam**.
8. Answer the questions and submit. The result page displays the score and congratulations when the percentage is at least 70%.

Capture `03-admin-site.png` only after your admin page visibly shows both Authentication and Authorization and Onlinecourse sections. Capture `07-final.png` from the actual result page after submitting a mock exam.
