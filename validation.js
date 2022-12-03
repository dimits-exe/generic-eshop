const passwordField  = document.getElementById("signup-password");
const passwordConfirmField = document.getElementById("signup-password-2nd");
const birthdateField = document.getElementById("signup-birthdate");

const paymentMethod = document.getElementById("payment-methods");
const paymentDetails = document.getElementById("payment-details")

const signUpButton = document.getElementById("sign-up-button");

signUpButton.onclick = () => {
    checkPasswords();
    checkPayment();
    checkBirthDate();
}

/**
 * Checks if the two password fields are equal.
 */
function checkPasswords() {
    let errorMsg = "";

    if(passwordField.value !== passwordConfirmField.value){
        errorMsg = "Passwords must match";
    }

    passwordField.setCustomValidity(errorMsg);
    passwordConfirmField.setCustomValidity(errorMsg);
}

/**
 * Checks if the payment details field is filled if the customer hasn't selected "cash only".
 */
function checkPayment() {
    let method = paymentMethod.value;
    let details = paymentDetails.value;
    let errorMsg = "";
    
    if(method.value !== "Pay With Cash" && details.value === "") {
        errorMsg = "Please fill in the details of your payment";
    }
    paymentDetails.setCustomValidity(errorMsg);
}

/**
 * Checks if the birthdate isn't after the current date or the signee is under 18 yo.
 */
function checkBirthDate() {
    let birthdate = birthdateField.value;
    let todaysDate = new Date();
    let errorMsg = "";

    if(birthdate >= todaysDate) {
        errorMsg = "Please enter a valid date";
    } else if (calculateAge(birthdate) < 18) {
        errorMsg = "You have to be 18+ to register"
    }

    birthdateField.setCustomValidity(errorMsg);
}

/**
 * Calculate the age of a person based on their birthday.
 * @param {Date} birthday the person's birthday  
 * @returns the age of the person in years
 */
function calculateAge(birthday) {
    let ageDifMs = Date.now() - birthday;
    let ageDate = new Date(ageDifMs);
    return Math.abs(ageDate.getUTCFullYear() - 1970);
}
