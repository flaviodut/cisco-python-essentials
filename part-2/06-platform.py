from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

print(platform())
print(platform(1))
print(platform(0, 1)) # concise

print(machine()) # arq
print(processor()) # processor
print(system()) # generic OS name
print(version()) # OS version

print(python_implementation(), python_version_tuple())
