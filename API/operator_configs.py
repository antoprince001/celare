from presidio_anonymizer.entities import OperatorConfig

operators_for_mask = {
  "DEFAULT": OperatorConfig("mask", {"masking_char": "*", "chars_to_mask": 20, "from_end": False}),
  "PHONE_NUMBER": OperatorConfig("mask", {"masking_char": "*", "chars_to_mask": 15, "from_end": False}),
  "EMAIL_ADDRESS": OperatorConfig("mask", {"masking_char": "*", "chars_to_mask": 20, "from_end": False}),
  "PERSON": OperatorConfig("mask", {"masking_char": "*", "chars_to_mask": 20, "from_end": False}),
}

operators_for_hash = {
  "DEFAULT": OperatorConfig("hash", {}),
  "PHONE_NUMBER": OperatorConfig("hash", {}),
  "TITLE": OperatorConfig("hash", {}),
  "EMAIL_ADDRESS": OperatorConfig("hash", {}),
  "PERSON": OperatorConfig("hash", {})
}

operators_for_redact = {
  "DEFAULT": OperatorConfig("redact", {}),
  "PHONE_NUMBER": OperatorConfig("redact", {}),
  "TITLE": OperatorConfig("redact", {}),
  "EMAIL_ADDRESS": OperatorConfig("redact", {}),
  "PERSON": OperatorConfig("redact", {})
}

operators_for_replace = {
  "DEFAULT": OperatorConfig("replace", {"new_value": "<REDACTED>"}),
  "PHONE_NUMBER": OperatorConfig("replace", {"new_value": "<PHONE_NUMBER>"}),
  "TITLE": OperatorConfig("replace", {"new_value": "<TITLE>"}),
  "EMAIL_ADDRESS": OperatorConfig("replace", {"new_value": "<EMAIL>"}),
  "PERSON": OperatorConfig("replace", {"new_value": "<PERSON>"})
}

operator_configs = {
    "mask": operators_for_mask,
    "hash": operators_for_hash,
    "redact": operators_for_redact,
    "replace": operators_for_replace
}
