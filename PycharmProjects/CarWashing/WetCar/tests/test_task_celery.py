from WetCar.tasks import test_task
result = test_task.delay()
print(result.get(timeout=10))
