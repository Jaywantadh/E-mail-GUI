# Email Scheduler Application
---

## Overview

The Email Scheduler Application is a desktop application built with Python and Tkinter that allows users to schedule and send emails with attachments. It features a user-friendly GUI to input email details, attach files, and set scheduling preferences. The application also includes a dark mode theme for enhanced usability.

## Features

- **Email Input**: Enter sender's email and app password.
- **Recipient Emails**: Input one or multiple recipient email addresses.
- **Body Message**: Write the email body message.
- **File Attachment**: Attach files to the email.
- **Scheduling**: Set interval for repeated emails or schedule an email for a specific date and time.
- **Theme Toggle**: Switch between light and dark modes.
- **Start/Cancel**: Start and stop email sending.

## Installation

Ensure you have Python installed on your system. You will need to install the following packages:

- `tkinter`
- `tkcalendar`
- `schedule`

You can install the necessary packages using pip:

```bash
pip install tkcalendar schedule
```

## Usage

1. **Running the Application**

   Run the script to start the application:

   ```bash
   python email_scheduler.py
   ```

2. **Using the Application**

   - **Sender's Email**: Enter the sender's email address.
   - **App Password**: Enter the app password for the sender's email account.
   - **Recipient's Email(s)**: Enter the recipient email addresses, separated by commas.
   - **Body Message**: Write the content of the email.
   - **Attach File**: Click the "Attach File" button to select a file to attach.
   - **Interval (seconds)**: Enter the interval in seconds for repeated email sending, or leave it blank for scheduling.
   - **Select Date**: Choose the date for scheduling the email.
   - **Select Time (HH:MM:SS)**: Enter the time for scheduling the email.
   - **Switch Theme**: Toggle between light and dark modes using the "Switch Theme" button.
   - **Start**: Click "Start" to begin sending emails according to the specified schedule.
   - **Cancel**: Click "Cancel" to stop scheduled email sending.
   - **Exit**: Click "Exit" to close the application.

## Code Structure

- `EmailSchedulerApp` Class: Contains the main functionality and GUI components.
- `attach_file()`: Opens a file dialog to select a file for attachment.
- `send_email()`: Sends the email using SMTP with the provided details.
- `schedule_email()`: Handles the scheduling of the email.
- `get_scheduled_time()`: Retrieves the scheduled time from the calendar and time entry.
- `start_sending()`: Starts the email sending process based on the interval or scheduled time.
- `cancel_sending()`: Cancels any ongoing scheduled email sending.
- `switch_theme()`: Switches between light and dark themes.
- `configure_theme()`: Applies the selected theme to the application.

## Dependencies

- `tkinter`: For creating the GUI.
- `tkcalendar`: For the calendar widget.
- `schedule`: For scheduling tasks.
- `smtplib`, `email`: For sending emails.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Tkinter for GUI development.
- `tkcalendar` for the calendar widget.
- `schedule` for task scheduling.
