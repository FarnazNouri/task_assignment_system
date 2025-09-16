from Service.task_service import TaskService
from Service.user_service import UserService

def main():
    task_service = TaskService()
    user_service = UserService()

    user_service.add_user(123,'farnaz','farnaz@gmail.com')
    
    task_service.create_task(1, 'learn data structure', 'scratch')
    task_service.create_task(2,'practice with leetcode', 'practive part')
    task_service.create_task(3, 'do a project', 'scratch')
    task_service.create_task(4, 'push to github', 'commit')

    completed_task = task_service.complete_task()
    print(completed_task)

    completed_task = task_service.complete_task()
    print(completed_task)


    history = task_service.get_task_history()
    while not history.is_empty():
        print(history.pop().title)

if __name__ == "__main__":
    main()