{
	"info": {
		"_postman_id": "43f888bc-7053-45d3-a56a-1b83a9fa8932",
		"name": "Research_Portal_API",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "58657762",
		"_collection_link": "https://musadiqzeb12356-8100065.postman.co/workspace/Musadiq-Zeb's-Workspace~fc50985d-54a3-49e0-8c70-98528a6c820f/collection/58657762-43f888bc-7053-45d3-a56a-1b83a9fa8932?action=share&source=collection_link&creator=58657762"
	},
	"item": [
		{
			"name": "Get All Opportunities",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/api/opportunities",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"opportunities"
					]
				}
			},
			"response": []
		},
		{
			"name": "Get One Opportunity",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/api/opportunities/1",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"opportunities",
						"1"
					]
				}
			},
			"response": []
		},
		{
			"name": "Create Oppotunity",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"title\": \"Quantum Computing Lab Assistant\",\n    \"description\": \"Running simulations on quantum algorithms.\",\n    \"research_area\": \"Physics & Computer Science\",\n    \"faculty_name\": \"Dr. Richard Feynman\",\n    \"department\": \"Physics\",\n    \"required_skills\": \"Python, Qiskit\",\n    \"available_positions\": 1,\n    \"application_deadline\": \"2026-12-01\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/opportunities",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"opportunities"
					]
				}
			},
			"response": []
		},
		{
			"name": "Update Opportunity",
			"request": {
				"method": "PUT",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"status\": \"Closed\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/opportunities/1",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"opportunities",
						"1"
					]
				}
			},
			"response": []
		},
		{
			"name": "Delete Oppotunity",
			"request": {
				"method": "DELETE",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/api/opportunities/2",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"opportunities",
						"2"
					]
				}
			},
			"response": []
		}
	]
}