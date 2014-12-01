# Makefile: For Python3 development.
# Because fabric doesn't work in Py3 :(

.PHONY: clean demo demo_server

clean:
	rm -rf "dist" \
		"build" \
		"demo/build" \
		"sphinx_bootstrap_theme.egg-info" \

demo:
	cd demo && make html

demo_server:
	cd demo/build/html && python -m http.server 8000
