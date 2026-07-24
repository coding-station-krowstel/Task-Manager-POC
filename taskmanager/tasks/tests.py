from django.test import TestCase
from .models import Task
from rest_framework.test import APIClient

class TaskTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_task(self):
        response = self.client.post("/tasks/",
        {
            "title" : "Learn Django",
            "description" : "Learn DRF Testing",
            "status" : "Pending"        
        }
        )
        self.assertEqual(response.status_code,201)
        self.assertEqual(Task.objects.count(),1)

    def test_create_task_without_title(self):
        response = self.client.post(
            "/tasks/",
            {
                "title" : "    ",
                "description" : "Testing Validation",
                "status" : "Pending"
            }
        )
        self.assertEqual(response.status_code,400)
        self.assertEqual(Task.objects.count(),0)  

    def test_get_task_list(self):
        task = Task.objects.create(
            title = "Learn Django",
            description = "Learn DRF Testing",
            status = "Pending"   
        )
        response = self.client.get(f"/tasks/{task.pk}/")
        self.assertEqual(response.data["title"],"Learn Django")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['description'],"Learn DRF Testing")  

    def test_update_task(self):
        task = Task.objects.create(
            title = "Learn Django",
            description = "Learn DRF Testing",
            status = "Pending"   
        )
        update_data = {
            "title" : "Learn Django Updated",
            "description" : "Updated Description",
            "status" : "Completed"
        } 
        response = self.client.put(f"/tasks/{task.pk}/",update_data, format = "json")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["title"],"Learn Django Updated")
        self.assertEqual(response.data["description"],"Updated Description")


    def test_delete_task(self):
        task = Task.objects.create(
            title = "Learn Django",
            description = "Learn DRF Testing",
            status = "Pending"   
        ) 
        response = self.client.delete(f"/tasks/{task.pk}/")
        self.assertEqual(response.status_code,204)
        self.assertEqual(Task.objects.count(),0)

    def test_get_nonexistent(self):
        response = self.client.get("/tasks/999/")
        self.assertEqual(response.status_code,404)  

    def test_invalid_update_task(self):
        task = Task.objects.create(
            title = "Learn Django",
            description = "Learn DRF Testing",
            status = "Pending"   
        )
        update_data = {
            "title" : "    ",
            "description" : "Updated Description",
            "status" : "Completed"
        } 
        response = self.client.put(f"/tasks/{task.pk}/",update_data,format="json")
        self.assertEqual(response.status_code,400)
