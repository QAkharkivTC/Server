import requests
import time
import traceback

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"})
session.cookies["PHPSESSID"] = "8ae11891dc704879b18c4d4c28230445"

summary = {"Error": 0}
for i in range(0, 15, 1):
	time.sleep(1)
	try:
		request = session.get("http://10.110.15.219/api/v3.1/users?&page_size=1000")
	except Exception as exc:
		print(traceback.format_exc())
		summary["Error"] += 1
		continue
	if request.status_code != 200:
		print("Request failed with status code %d." % request.status_code)
		print(request.text)
		summary["Error"] += 1
		continue
	result = None
	try:
		result = request.json()
	except Exception as exc:
		print(traceback.format_exc())
		result["Error"] += 1
		continue
	if "next_page_id" not in result or "users" not in result:
		print(traceback.format_exc())
		print(request.text)
		result["Error"] += 1
		continue
	key = len(result["users"])
	if key not in summary:
		summary[key] = 0
	summary[key] += 1
	print(result["next_page_id"], len(result["users"]))
print(summary)
