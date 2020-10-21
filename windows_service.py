import psutil

# Only works for windows users.
# Althouth it might not working well
# Cause psutil older versions only support
# this methods.

print(list(psutil.win_service_iter()))

s = psutil.win_service_get('alg')
print(s.as_dict())
