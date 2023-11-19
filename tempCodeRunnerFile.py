# get the job_code for 'Database Designer'
target_job = session.query(Job).filter(Job.job_description == 'Database Designer').first()
print(target_job.job_code)

employee = session.query(Employee).filter(Employee.emp_num == 168).first()
employee.job_code = target_job.job_code
session.commit()