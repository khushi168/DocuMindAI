const form = document.getElementById("uploadForm");

const fileInput = document.getElementById("file-upload");

const fileName = document.getElementById("file-name");

fileInput.addEventListener("change", () => {

    if (fileInput.files.length > 0) {

        fileName.textContent =
            fileInput.files[0].name;

    }

});

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const loading =
        document.getElementById("loading");

    loading.style.display = "block";

    const formData =
        new FormData(form);

    const response = await fetch("/upload", {

        method: "POST",

        body: formData

    });

    const data = await response.json();

    loading.style.display = "none";

    renderDashboard(data);

});

function renderDashboard(data) {

    const result =
        document.getElementById("result");

    /*
    =====================================
    MEETING NOTES DASHBOARD
    =====================================
    */

    if (data.document_type === "Meeting Notes") {

        result.innerHTML = `

        <div class="dashboard-grid">

            <div class="dashboard-card">

                <h2>Meeting Summary</h2>

                <p>${data.summary || "Not Found"}</p>

            </div>

            <div class="dashboard-card">

                <h2>Attendees</h2>

                <ul>

                    ${renderList(data.attendees)}

                </ul>

            </div>

            <div class="dashboard-card">

                <h2>Discussion Points</h2>

                <ul>

                    ${renderList(data.discussion_points)}

                </ul>

            </div>

            <div class="dashboard-card">

                <h2>Action Items</h2>

                <ul>

                    ${renderList(data.action_items)}

                </ul>

            </div>

            <div class="dashboard-card">

                <h2>Deadlines</h2>

                <ul>

                    ${renderList(data.deadlines)}

                </ul>

            </div>

        </div>

        `;

    }

    /*
    =====================================
    RESUME DASHBOARD
    =====================================
    */

    else if (data.document_type === "Resume") {

        result.innerHTML = `

        <div class="dashboard-grid">

            <div class="dashboard-card">

                <h2>Candidate Information</h2>

                <p><strong>Name:</strong> ${data.name}</p>

                <p><strong>Email:</strong> ${data.email}</p>

                <p><strong>Phone:</strong> ${data.phone}</p>

            </div>

            <div class="dashboard-card">

                <h2>Technical Skills</h2>

                <ul>

                    ${renderList(data.skills)}

                </ul>

            </div>

            <div class="dashboard-card">

                <h2>Projects</h2>

                <ul>

                    ${renderList(data.projects)}

                </ul>

            </div>

            <div class="dashboard-card">

                <h2>Suggested Actions</h2>

                <ul>

                    <li>Review candidate profile</li>

                    <li>Schedule technical interview</li>

                    <li>Evaluate project experience</li>

                </ul>

            </div>

        </div>

        `;

    }

    /*
    =====================================
    OFFER LETTER DASHBOARD
    =====================================
    */

    else if (data.document_type === "Offer Letter") {

        result.innerHTML = `

        <div class="dashboard-grid">

            <div class="dashboard-card">

                <h2>Document Information</h2>

                <p><strong>Candidate:</strong> ${data.candidate_name}</p>

                <p><strong>Company:</strong> ${data.company}</p>

                <p><strong>Role:</strong> ${data.role}</p>

            </div>

            <div class="dashboard-card">

                <h2>Compensation</h2>

                <p><strong>CTC:</strong> ${data.ctc}</p>

                <p><strong>Bond:</strong> ${data.bond}</p>

                <p><strong>Penalty:</strong> ${data.penalty}</p>

            </div>

            <div class="dashboard-card">

                <h2>Required Documents</h2>

                <ul>

                    ${renderList(data.required_documents)}

                </ul>

            </div>

            <div class="dashboard-card">

                <h2>Action Items</h2>

                <ul>

                    ${renderList(data.action_items)}

                </ul>

            </div>

        </div>

        `;

    }

    /*
    =====================================
    INVOICE DASHBOARD
    =====================================
    */

    else if (data.document_type === "Invoice") {

        result.innerHTML = `

        <div class="dashboard-grid">

            <div class="dashboard-card">

                <h2>Invoice Details</h2>

                <p><strong>Vendor:</strong> ${data.vendor}</p>

                <p><strong>Invoice Number:</strong> ${data.invoice_number}</p>

                <p><strong>Amount:</strong> ${data.amount}</p>

            </div>

            <div class="dashboard-card">

                <h2>Payment Information</h2>

                <p><strong>Invoice Date:</strong> ${data.invoice_date}</p>

                <p><strong>Due Date:</strong> ${data.due_date}</p>

                <p><strong>Bank Name:</strong> ${data.bank_name}</p>

            </div>

            <div class="dashboard-card">

                <h2>Recommended Actions</h2>

                <ul>

                    <li>Verify invoice details</li>

                    <li>Approve payment</li>

                    <li>Process vendor transaction</li>

                </ul>

            </div>

        </div>

        `;

    }

    /*
    =====================================
    FALLBACK
    =====================================
    */

    else {

        result.innerHTML = `

        <div class="dashboard-card">

            <h2>General Document</h2>

            <p>No structured parser available.</p>

        </div>

        `;
    }
}

function renderList(items) {

    if (!items || items.length === 0) {

        return "<li>Not Found</li>";

    }

    return items.map(item =>
        `<li>${item}</li>`
    ).join("");

}