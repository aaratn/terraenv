PLATFORM?=linux

build:
	@PYTHONOPTIMIZE=1 pyinstaller terraenv.py --onefile --clean --osx-bundle-identifier com.aarat.os.terraenv --nowindowed
package:
	tar -czvf ./terraenv_$(PLATFORM).tar.gz dist/terraenv