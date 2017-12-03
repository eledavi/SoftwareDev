package com.example2.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;

import java.sql.Date;

public class Profile extends AppCompatActivity {

    private TextView mTextMessage;
    private String name;
    private Date bdate;
    private String email;

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            switch (item.getItemId()) {
                case R.id.navigation_home:
                    goToHome();
                    return true;
                case R.id.navigation_groups:
                    goToGroups();
                    return true;
                case R.id.navigation_notifications:
                    goToNotifications();
                    return true;
                case R.id.navigation_profile:
                    name = "Bob";
                    email = "email@nmsu.edu";
                    mTextMessage.setText(R.string.title_activity_profile);
                    mTextMessage.setText("Name: "+name+"\n\nEmail: "+email);
                    return true;
            }
            return false;
        }

    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);

        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);
        navigation.setSelectedItemId(R.id.navigation_profile);
    }

    public void goToHome () {
        Intent home = new Intent(this, Home.class);
        startActivity(home);
    }

    public void goToGroups () {
        Intent group = new Intent(this, Groups.class);
        startActivity(group);
    }

    public void goToNotifications () {
        Intent notific = new Intent(this, Notifications.class);
        startActivity(notific);
    }

    public void goToProfile () {
        Intent profile = new Intent(this, Profile.class);
        startActivity(profile);
    }

}
