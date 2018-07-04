import requests

APEX_VALUES          = None
CNAME_VALUE          = [".cloudfront.net"]
RESPONSE_FINGERPRINT = "The request could not be satisfied"

def detector(domain, ip, cname):
	if APEX_VALUES:
		if ip in APEX_VALUES:
			return True
	if filter(lambda x: x in cname, CNAME_VALUE):
		try:
			if RESPONSE_FINGERPRINT in requests.get('http://%s' % domain).text:
				return True
		except Exception as e:
			pass
	return False