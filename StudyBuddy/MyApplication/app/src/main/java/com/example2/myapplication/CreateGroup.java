package com.example2.myapplication;

import android.app.Activity;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;

/**
 * Created by elenadavidson on 12/2/17.
 */

public class CreateGroup extends AppCompatActivity {
    private TextView mTextMessage;

    

        private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
                = new BottomNavigationView.OnNavigationItemSelectedListener() {

            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                {
                    switch (item.getItemId()) {
                        case R.id.navigation_home:
                            mTextMessage.setText(R.string.title_home);
                            return true;
                        case R.id.navigation_groups:
                            mTextMessage.setText("Groups");
                            return true;
                        case R.id.navigation_profile:
                            mTextMessage.setText("Profile");
                            return true;
                        case R.id.navigation_notifications:
                            mTextMessage.setText(R.string.title_notifications);
                            return true;
                    }
                    return false;
                }

            }

            ;
        };
    }
