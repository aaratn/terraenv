PLATFORM?=linux_x64

build:
	@PYTHONOPTIMIZE=1 pyinstaller terraenv --onefile --clean --osx-bundle-identifier com.aarat.os.terraenv --nowindowed
	@chmod +x dist/terraenv

package:
	@cd dist && tar -czvf ./terraenv_$(PLATFORM).tar.gz terraenv

build-pip:
	@rm -rf dist/
	@python3 setup.py bdist_wheel

upload-pip-test:
	@python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload-pip:
	@python3 -m twine upload dist/*