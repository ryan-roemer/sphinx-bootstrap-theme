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

# PORT allows you to specify a different port if say
# port 8000 is currently in use
#
# make demo_server PORT=8080
PORT ?= 8000
demo_server: demo
	cd demo/build/html && python3 -m http.server $(PORT)
