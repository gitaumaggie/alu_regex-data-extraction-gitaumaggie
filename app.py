
import streamlit as st

from validators import (
    validate_email,
    validate_url,
    validate_phone,
    validate_credit_card,
    validate_time,
    validate_html_tag,
    validate_hashtag,
    validate_currency
)

# Configure the application
st.set_page_config(
    page_title="Regex Data Validator",
    page_icon="🔍",
    layout="centered"
)

# Application heading
st.title("Regex Data Validator")

st.write(
    "Validate different types of data using "
    "regular expressions."
)

# Connect validation categories to their functions
validators = {
    "Email Address": validate_email,
    "URL": validate_url,
    "Phone Number": validate_phone,
    "Credit Card Number": validate_credit_card,
    "Time": validate_time,
    "HTML Tag": validate_html_tag,
    "Hashtag": validate_hashtag,
    "Currency Amount": validate_currency
}

# Expected formats and examples
guidance = {
    "Email Address": {
        "description": "Enter an email address.",
        "example": "username@example.com"
    },
    "URL": {
        "description": (
            "Enter a URL beginning with "
            "http:// or https://."
        ),
        "example": "https://www.example.com"
    },
    "Phone Number": {
        "description": (
            "Use one of the accepted phone number formats."
        ),
        "example": "(123) 456-7890"
    },
    "Credit Card Number": {
        "description": (
            "Enter 16 digits using consistent "
            "spaces or hyphens."
        ),
        "example": "1234-5678-9012-3456"
    },
    "Time": {
        "description": (
            "Use 12-hour format with AM/PM, "
            "or 24-hour format without AM/PM."
        ),
        "example": "02:30 PM or 14:30"
    },
    "HTML Tag": {
        "description": "Enter a valid-looking HTML tag.",
        "example": '<div class="example">'
    },
    "Hashtag": {
        "description": (
            "Start with # followed by letters, "
            "numbers or underscores."
        ),
        "example": "#MyHashtag"
    },
    "Currency Amount": {
        "description": (
            "Enter the amount without the dollar sign. "
            "Use exactly two decimal places."
        ),
        "example": "1234.56 or 1,234.56"
    }
}

# Select validation category
validation_type = st.selectbox(
    "Choose a validation type:",
    list(validators.keys())
)

# Display instructions for the selected category
st.caption(
    guidance[validation_type]["description"]
)

st.caption(
    f'Example: {guidance[validation_type]["example"]}'
)

# Collect user input
if validation_type == "Currency Amount":

    st.write("Enter the currency amount:")

    # CSS styling for the currency symbol
    st.markdown(
        """
        <style>
        .currency-row {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .currency-symbol {
            font-size: 24px;
            font-weight: 600;
            margin-top: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    dollar_column, input_column = st.columns([0.08, 0.92])

    with dollar_column:
        st.markdown(
            '<div class="currency-symbol">$</div>',
            unsafe_allow_html=True
        )

    with input_column:
        user_input = st.text_input(
            "Currency amount",
            placeholder="1234.56",
            label_visibility="collapsed",
            help="Enter the amount without the dollar sign."
        )

else:
    user_input = st.text_input(
        "Enter the value you want to validate:"
    )

# Validate input when button is clicked
if st.button("Validate"):

    if not user_input.strip():

        st.warning(
            "Input required: Please enter a value "
            "before validating."
        )

    else:
        # Remove unnecessary surrounding spaces
        cleaned_input = user_input.strip()

        # Automatically add dollar sign for currency
        if validation_type == "Currency Amount":
            value_to_validate = "$" + cleaned_input
        else:
            value_to_validate = cleaned_input

        # Execute the selected validator
        validator = validators[validation_type]

        result = validator(value_to_validate)

        # Display validation result
        if result:

            st.success(
                "Validation successful! "
                f"Your {validation_type.lower()} follows "
                "the expected format."
            )

            # Display the validated value
            if validation_type == "Currency Amount":
                display_value = "$" + cleaned_input
            else:
                display_value = cleaned_input

            st.write(
                f"Validated input: `{display_value}`"
            )

        else:

            st.error(
                "Validation failed! "
                f"Your {validation_type.lower()} does not "
                "follow the expected format."
            )

            st.info(
                "Expected format: "
                f"{guidance[validation_type]['example']}"
            )
