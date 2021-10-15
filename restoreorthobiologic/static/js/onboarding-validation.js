// DATE OF BIRTH CALCULATION
function calculateAge() {
    const today = new Date();
    const currentDate = (today.getMonth() + 1) + '-' + today.getDate() + '-' + today.getFullYear();
    const currentDateParts = currentDate.split('-');
    const dateOfBirth = document.getElementById("date_of_birth").value;
    const dateOfBirthParts = dateOfBirth.split('-');
    const monthDiff = currentDateParts[0] - dateOfBirthParts[0];
    let age = currentDateParts[2] - dateOfBirthParts[2];
    if (monthDiff < 0 || (monthDiff === 0 && currentDateParts[1] < dateOfBirthParts[1])) {
        age--;
    }
    document.getElementById("age-input").value = age;
}

// GENDER PRONOUN ASSIGNMENT
function genderPronoun() {
    let genderSelection = document.getElementById('gender');
    if (genderSelection.value === 'Male') {
        document.getElementById('he_or_she').value = 'he';
        document.getElementById('him_or_her').value = 'him';
        document.getElementById('his_or_her').value = 'his';
    } else if (genderSelection.value === 'Female') {
        document.getElementById('he_or_she').value = 'she';
        document.getElementById('him_or_her').value = 'her';
        document.getElementById('his_or_her').value = 'her';
        console.log('Gender Pronouns: Female')
    } else {
        document.getElementById('he_or_she').value = 'they';
        document.getElementById('him_or_her').value = 'they';
        document.getElementById('his_or_her').value = 'their';
        console.log('Gender Pronouns: Neutral')
    }
}

// IF PHYSICAL ADDRESS IS SAME AS MAILING, DISABLE PHYSICAL ADDRESS FIELDS AND UPDATE TO SAME VALUE
function physicalAddressSame() {
    let sameAddress = document.getElementById('address_same_check');
    let mailingAddress = document.getElementById('mailing_address');
    let mailingCity = document.getElementById('mailing_city');
    let mailingState = document.getElementById('mailing_state');
    let mailingZip = document.getElementById('mailing_zip');
    let streetAddress = document.getElementById('street_address');
    let streetCity = document.getElementById('street_city');
    let streetState = document.getElementById('street_state');
    let streetZip = document.getElementById('street_zip');
    if (sameAddress.checked === true) {
        streetAddress.value = mailingAddress.value;
        streetCity.value = mailingCity.value;
        streetState.value = mailingState.value;
        streetZip.value = mailingZip.value;
        streetAddress.readOnly = true;
        streetCity.readOnly = true;
        streetState.readOnly = true;
        streetZip.readOnly = true;
    } else {
        streetAddress.readOnly = false;
        streetAddress.value = '';
        streetCity.readOnly = false;
        streetCity.value = '';
        streetState.readOnly = false;
        streetState.value = '';
        streetZip.readOnly = false;
        streetZip.value = '';
    }
}

// RESPONSIBLE PARTY FIELD SHOW/HIDE
function selfResponsible() {
    let isResponsible = document.getElementById('resp_pty_self_radio_yes');
    if (isResponsible.checked === true) {
        document.getElementById('resp_pty_name').value = 'Self';
        document.getElementById('resp_pty').hidden = true;
        document.getElementById('resp_pty_name').required = false;
        document.getElementById('resp_pty_dob').required = false;
        document.getElementById('resp_pty_cell_ph').required = false;
    } else {
        document.getElementById('resp_pty_name').value = '';
        document.getElementById('resp_pty').hidden = false;
        document.getElementById('resp_pty_name').required = true;
        document.getElementById('resp_pty_dob').required = true;
        document.getElementById('resp_pty_cell_ph').required = true;
    }
}

// SURGERY FIELD SHOW/HIDE
function hadSurgery() {
    let surgicalHistory = document.getElementById('surgery_yes_no');
    if (surgicalHistory.value === 'Yes') {
        document.getElementById('srg_list_input').hidden = false;
        document.getElementById('srg_list').required = true;
    } else {
        document.getElementById('srg_list_input').hidden = true;
        document.getElementById('srg_list').value = 'NO SURGICAL HISTORY REPORTED';
        document.getElementById('srg_list').required = false;
    }
}

// MEDICATION FIELD SHOW/HIDE
function takesMedication() {
    let surgicalHistory = document.getElementById('medication_yes_no');
    if (surgicalHistory.value === 'Yes') {
        document.getElementById('med_list_input').hidden = false;
        document.getElementById('med_list').required = true;
    } else {
        document.getElementById('med_list_input').hidden = true;
        document.getElementById('med_list').value = 'NKM';
        document.getElementById('med_list').required = false;
    }
}

// ALLERGY FIELD SHOW/HIDE
function hasAllergies() {
    let surgicalHistory = document.getElementById('allergies_yes_no');
    if (surgicalHistory.value === 'Yes') {
        document.getElementById('alg_list_input').hidden = false;
        document.getElementById('alg_list').required = true;
    } else {
        document.getElementById('alg_list_input').hidden = true;
        document.getElementById('alg_list').value = 'NKDA';
        document.getElementById('alg_list').required = false;
    }
}

// TOBACCO USE FIELD SHOW/HIDE
function useTobacco() {
    let tobaccoUse = document.getElementById('tobacco');
    if (tobaccoUse.value === 'Yes') {
        document.getElementById('tobacco-type-select').hidden = false;
        document.getElementById('tobacco_type').required = true;
        document.getElementById('tobacco-you').hidden = false;
        document.getElementById('tobacco_years').required = true;
    } else {
        document.getElementById('tobacco-type-select').hidden = true;
        document.getElementById('tobacco_type').required = false;
        document.getElementById('tobacco_type').value = 'N/A';
        document.getElementById('tobacco-you').hidden = true;
        document.getElementById('tobacco_years').required = false;
        document.getElementById('tobacco_years').value = 'N/A';
    }
}

// LEARNING BARRIERS CHECKBOX DISABLE IF NONE
function noLearningBarriers() {
    let learningBarriersNone = document.getElementById('lb_none');
    if (learningBarriersNone.checked === true) {
        document.getElementById('lb_age').checked = false;
        document.getElementById('lb_mental').checked = false;
        document.getElementById('lb_language').checked = false;
        document.getElementById('lb_hearing').checked = false;
        document.getElementById('lb_financial').checked = false;
        document.getElementById('lb_education').checked = false;
        document.getElementById('lb_age').disabled = true;
        document.getElementById('lb_mental').disabled = true;
        document.getElementById('lb_language').disabled = true;
        document.getElementById('lb_hearing').disabled = true;
        document.getElementById('lb_financial').disabled = true;
        document.getElementById('lb_education').disabled = true;
    } else {
        document.getElementById('lb_age').disabled = false;
        document.getElementById('lb_mental').disabled = false;
        document.getElementById('lb_language').disabled = false;
        document.getElementById('lb_hearing').disabled = false;
        document.getElementById('lb_financial').disabled = false;
        document.getElementById('lb_education').disabled = false;
    }
}

// LEARNING PREFERENCE CHECKBOX DISABLE IF NONE
function noLearningPreference() {
    let learningPreferenceNone = document.getElementById('ls_np');
    if (learningPreferenceNone.checked === true) {
        document.getElementById('ls_doing').checked = false;
        document.getElementById('ls_hearing').checked = false;
        document.getElementById('ls_reading').checked = false;
        document.getElementById('ls_seeing').checked = false;
        document.getElementById('ls_doing').disabled = true;
        document.getElementById('ls_hearing').disabled = true;
        document.getElementById('ls_reading').disabled = true;
        document.getElementById('ls_seeing').disabled = true;
    } else {
        document.getElementById('ls_doing').disabled = false;
        document.getElementById('ls_hearing').disabled = false;
        document.getElementById('ls_reading').disabled = false;
        document.getElementById('ls_seeing').disabled = false;
    }
}

// INSURANCE SHOW/HIDE FIELDS BASED ON INPUT
function haveInsurance() {
    let hasInsurance = document.getElementById('insurance_radio_yes');
    document.getElementById('primary_insurance').hidden = hasInsurance.checked !== true;
    document.getElementById('insurance_secondary_radio_yes').hidden = hasInsurance.checked !== true;
    document.getElementById('insurance_secondary_radio_yes').required = hasInsurance.checked !== false;
    document.getElementById('secondary_insurance_radio').hidden = hasInsurance.checked !== true;
}

// SECONDARY INSURANCE SHOW/HIDE FIELDS BASED ON INPUT
function haveSecondaryInsurance() {
    let hasSecondaryInsurance = document.getElementById('insurance_secondary_radio_yes');
    document.getElementById('secondary_insurance').hidden = hasSecondaryInsurance.checked !== true;
}

// CHANGE FIELD INPUT BASED ON SYMPTOM DURATION SELECTION
function symptomDuration() {
    let hasSymptoms = document.getElementById('symptom_dur');
    if (hasSymptoms.value === 'Days' || 'Months' || 'Weeks' || 'Years') {
        document.getElementById('symptom_dur_num_input').hidden = false;
        document.getElementById('symptom_dur_num').required = true;
        document.getElementById('symptom_dur_num').placeholder = "How many " + hasSymptoms.value + "?";
        document.getElementById('symptom_dur_num_label').innerHTML = "How many " + hasSymptoms.value + "?";
    } else if (hasSymptoms.value === '') {
        document.getElementById('symptom_dur_num_input').hidden = true;
        document.getElementById('symptom_dur_num').required = false;
    }
}

// IF INJURY, SHOW INJURY DATE FIELD
function isInjury() {
    let wasInjury = document.getElementById('reason_cause');
    if (wasInjury.value === 'Specific Injury') {
        document.getElementById('date_of_injury_input').hidden = false;
        document.getElementById('date_of_injury_input').required = true;
    } else if (wasInjury.value === 'Injury at Work') {
        document.getElementById('date_of_injury_input').hidden = false;
        document.getElementById('date_of_injury_input').required = true;
    } else if (wasInjury.value === 'Auto Accident') {
        document.getElementById('date_of_injury_input').hidden = false;
        document.getElementById('date_of_injury_input').required = true;
    } else if (wasInjury.value === 'Recurring Injury') {
        document.getElementById('date_of_injury_input').hidden = false;
        document.getElementById('date_of_injury_input').required = true;
    } else {
        document.getElementById('date_of_injury_input').hidden = true;
        document.getElementById('date_of_injury_input').required = false;
        document.getElementById('doi').value = 'N/A';
    }
}

// IF PAIN RADIATION, SHOW RADIATION LOCATION INPUT FIELD
function painRadiates() {
    let yesRadiates = document.getElementById('radiation_pain');
    if (yesRadiates.value === 'Yes') {
        document.getElementById('radiation_pain_input').hidden = false;
        document.getElementById('radiation_pain_location').required = true;
    } else {
        document.getElementById('radiation_pain_input').hidden = true;
        document.getElementById('radiation_pain_location').required = false;
    }
}

// AUTO CHECK INJECTION BOX IF INPUT IN ANY INJECTION FIELD
function injectionHistory() {
    document.getElementById('past_inj').checked = true;
}

// AUTO CHECK BRACE BOX IF INPUT IN ANY BRACE FIELD
function braceHistory() {
    document.getElementById('past_brace').checked = true;
}

// AUTO CHECK NSAID BOX IF INPUT IN ANY NSAID FIELD
function nsaidHistory() {
    document.getElementById('past_nsaid').checked = true;
}

// AUTO CHECK NARCOTICS BOX IF INPUT IN ANY NARCOTICS FIELD
function narcoticsHistory() {
    document.getElementById('past_narc').checked = true;
}

// AUTO CHECK PHYSICAL THERAPY BOX IF INPUT IN ANY PHYSICAL THERAPY FIELD
function ptHistory() {
    document.getElementById('past_pt').checked = true;
}