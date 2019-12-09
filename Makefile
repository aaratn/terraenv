PLATFORM?=linux_x64

build:
	@PYTHONOPTIMIZE=1 pyinstaller terraenv.py --onefile --clean --osx-bundle-identifier com.aarat.os.terraenv --nowindowed
	@chmod +x dist/terraenv

package:
	@cd dist && tar -czvf ./terraenv_$(PLATFORM).tar.gz terraenv