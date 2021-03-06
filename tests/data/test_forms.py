import pytest

from data.forms import (
    DatasetForm,
    VariableForm,
)

pytestmark = [pytest.mark.data, pytest.mark.form]


class TestDatasetForm:
    def test_form_with_invalid_data(self, invalid_dataset_data):
        form = DatasetForm(data=invalid_dataset_data)
        assert form.is_valid() is False
        expected_errors = {"name": ["This field is required."]}
        assert form.errors == expected_errors

    def test_form_with_valid_data(self, db, valid_dataset_data):
        form = DatasetForm(data=valid_dataset_data)
        assert form.is_valid() is True
        dataset = form.save()
        assert dataset.name == valid_dataset_data["dataset_name"]

    def test_form_with_valid_data_uppercase(self, db, valid_dataset_data):
        valid_dataset_data["dataset_name"] = "SOME-DATASET"
        form = DatasetForm(data=valid_dataset_data)
        assert form.is_valid() is True
        dataset = form.save()
        assert dataset.name == "some-dataset"


class TestVariableForm:
    def test_form_with_invalid_data(self, invalid_variable_data):
        form = VariableForm(data=invalid_variable_data)
        assert form.is_valid() is False
        expected_errors = {"name": ["This field is required."]}
        assert form.errors == expected_errors

    def test_form_with_valid_data(self, valid_variable_data):
        form = VariableForm(data=valid_variable_data)
        assert form.is_valid() is True
        variable = form.save()
        assert variable.name == valid_variable_data["variable_name"]
        assert variable.dataset.name == valid_variable_data["dataset_name"]

    def test_form_with_valid_data_with_concept(self, valid_variable_data):
        valid_variable_data['concept_name'] = 'some-concept'
        form = VariableForm(data=valid_variable_data)
        assert form.is_valid() is True
        variable = form.save()
        assert variable.name == valid_variable_data["variable_name"]
        assert variable.dataset.name == valid_variable_data["dataset_name"]
