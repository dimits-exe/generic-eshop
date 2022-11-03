@echo off
setlocal

CD %~dp0
SET generator=%cd%\template_generator.py
SET header_config=%cd%\header.html
SET footer_config=%cd%\footer.html

CD..
FOR %%f IN (.\*) DO (
	IF "%%~xf"==".html" python %generator% %%f %header_config% %footer_config%
)


