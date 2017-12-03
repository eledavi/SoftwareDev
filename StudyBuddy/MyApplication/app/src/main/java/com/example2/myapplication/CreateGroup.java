package com.example2.myapplication;

import android.app.Activity;
import android.icu.text.DateTimePatternGenerator;
import android.icu.text.RelativeDateTimeFormatter;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.text.TextUtils;
import android.view.MenuItem;
import android.view.View;
import android.widget.AutoCompleteTextView;
import android.widget.EditText;
import android.widget.TextView;

import java.util.Date;


public class CreateGroup extends AppCompatActivity {
    /*
     * Keep track of the group creation task to ensure we can cancel it if requested.
     */
    private SignUp.UserLoginTask mAuthTask = null;

    private TextView mTextMessage;
    private EditText mGroupNameView;
    private EditText mGroupDayView;
    private EditText mGroupTimeView;
    private EditText mGroupCourseNameView;
    private EditText mGroupCourseIDView;
    /**
     * Attempts to create a new study group.
     * If there are form errors (invalid date, missing fields, etc.), the
     * errors are presented and no actual group creation attempt is made.
     */
    private void createGroupAttempt() {
        if (mAuthTask != null) {
            return;
        }

        // Reset errors.
        mGroupNameView.setError(null);
        mGroupDayView.setError(null);
        mGroupTimeView.setError(null);
        mGroupCourseNameView.setError(null);
        mGroupCourseNameView.setError(null);

        // Store values at the time of the login attempt.
        String groupName = mGroupNameView.getText().toString();
        String day = mGroupDayView.getText().toString();
        String time = mGroupTimeView.getText().toString();
        String courseName = mGroupCourseNameView.getText().toString();
        String courseID = mGroupCourseIDView.getText().toString();

        boolean cancel = false;
        View focusView = null;

        if (TextUtils.isEmpty(groupName)) {
            mGroupNameView.setError("This field is required");
            focusView = mGroupNameView;
            cancel = true;
        }
        if (TextUtils.isEmpty(day)) {
            mGroupDayView.setError("This field is required");
            focusView = mGroupDayView;
            cancel = true;
        }
        if (TextUtils.isEmpty(time)) {
            mGroupTimeView.setError("This field is required");
            focusView = mGroupTimeView;
            cancel = true;
        }

        // Check for a valid day of the week.
        if (TextUtils.isEmpty(day)) {
            mGroupDayView.setError(getString(R.string.error_field_required));
            focusView = mGroupDayView;
            cancel = true;
        } else if (!isDayValid(day)) {
            mGroupDayView.setError(getString(R.string.error_invalid_email)+ ". You must input a " +
                    "valid day of the week.");
            focusView = mGroupDayView;
            cancel = true;
        }

        // Check for a valid time.
        if (TextUtils.isEmpty(time)) {
            mGroupTimeView.setError(getString(R.string.error_field_required));
            focusView = mGroupTimeView;
            cancel = true;
        } else if (!isTimeValid(day)) {
            mGroupTimeView.setError(getString(R.string.error_invalid_email)+ ". You must input a valid time.");
            focusView = mGroupTimeView;
            cancel = true;
        }

        if (cancel) {
            // There was an error; don't attempt login and focus the first
            // form field with an error.
            focusView.requestFocus();
        }
    }


    private boolean isDayValid(String day) {
        return day.equals("Monday")||day.equals("Tuesday")||day.equals("Wednesday")||
                day.equals("Thursday")||day.equals("Friday")||day.equals("Saturday")||
                day.equals("Sunnday");
    }

    private boolean isTimeValid(String time) {
        return time.contains(":") && (time.endsWith("am")||time.endsWith("AM")||
                time.endsWith("pm")||time.endsWith("PM"));
    }

    public void toCreateGroup(View view) {
    }
}
