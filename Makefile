serve:
	uv run jupyter lab

clean:
	uv run jupyter nbconvert --clear-output --inplace notebooks/*.ipynb
