// Load existing data from localStorage or default to empty array
let students = JSON.parse(localStorage.getItem('students')) || [];
let isEditing = false;

// --- DOM Elements ---
const studentForm = document.getElementById('studentForm');
const studentName = document.getElementById('studentName');
const studentID = document.getElementById('studentID');
const studentEmail = document.getElementById('studentEmail');
const studentDepartment = document.getElementById('studentDepartment');
const studentCity = document.getElementById('studentCity');
const studentPhone = document.getElementById('studentPhone');
const studentDOB = document.getElementById('studentDOB');
const studentIndex = document.getElementById('studentIndex');

const formTitle = document.getElementById('formTitle');
const submitBtn = document.getElementById('submitBtn');
const cancelBtn = document.getElementById('cancelBtn');
const studentTableBody = document.getElementById('studentTableBody');
const noDataMessage = document.getElementById('noDataMessage');
const themeToggle = document.getElementById('themeToggle');


function displayStudents() {
    studentTableBody.innerHTML = '';
    
    if (students.length === 0) {
        noDataMessage.style.display = 'block';
        return;
    }
    
    noDataMessage.style.display = 'none';

    students.forEach((student, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.department || ''}</td>
            <td>${student.city || ''}</td>
            <td>${student.email}</td>
            <td>${student.phone || ''}</td>
            <td>${student.dob || ''}</td>
            <td class="action-btns">
                <button class="btn btn-edit" onclick="editStudent(${index})">Edit</button>
                <button class="btn btn-delete" onclick="deleteStudent(${index})">Delete</button>
            </td>
        `;
        studentTableBody.appendChild(row);
    });
}


studentForm.addEventListener('submit', function(e) {
    e.preventDefault();

    const studentData = {
        name: studentName.value.trim(),
        id: studentID.value.trim(),
        email: studentEmail.value.trim(),
        department: studentDepartment.value.trim(),
        city: studentCity.value.trim(),
        phone: studentPhone.value.trim(),
        dob: studentDOB.value.trim()
    };

    if (isEditing) {
        // Update Operation
        const index = studentIndex.value;
        students[index] = studentData;
        isEditing = false;
    } else {
        // Create Operation
        // Check for duplicate ID
        const idExists = students.some(s => s.id === studentData.id);
        if (idExists) {
            alert("A student with this ID already exists!");
            return;
        }
        students.push(studentData);
    }

    saveAndRefresh();
    resetForm();
});


function editStudent(index) {
    isEditing = true;
    formTitle.textContent = "Edit Student Details";
    submitBtn.textContent = "Update Student";
    cancelBtn.style.display = "inline-block";

    // Fill form fields
    studentName.value = students[index].name;
    studentID.value = students[index].id;
    studentEmail.value = students[index].email;
    studentDepartment.value = students[index].department || '';
    studentCity.value = students[index].city || '';
    studentPhone.value = students[index].phone || '';
    studentDOB.value = students[index].dob || '';
    studentIndex.value = index;
}


function deleteStudent(index) {
    if (confirm("Are you sure you want to delete this student record?")) {
        students.splice(index, 1);
        saveAndRefresh();
        if (isEditing) resetForm(); // Reset form if deleting while editing
    }
}


function saveAndRefresh() {
    localStorage.setItem('students', JSON.stringify(students));
    displayStudents();
}

function resetForm() {
    studentForm.reset();
    isEditing = false;
    formTitle.textContent = "Add New Student";
    submitBtn.textContent = "Add Student";
    cancelBtn.style.display = "none";
    studentIndex.value = "";
}

// --- Theme Toggle logic ---
// Check saved preference or default to light mode
const currentTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', currentTheme);

themeToggle.addEventListener('click', () => {
    let theme = document.documentElement.getAttribute('data-theme');
    let newTheme = (theme === 'dark') ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
});

// Initial load
displayStudents();