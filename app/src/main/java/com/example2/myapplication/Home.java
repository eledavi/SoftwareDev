package com.example2.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.IdRes;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.SearchView;
import android.support.v7.widget.Toolbar;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;

public class Home extends AppCompatActivity {

    private TextView mTextMessage;
    private Toolbar toolBar;


    public BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {

            switch (item.getItemId()) {
                case R.id.navigation_home:
                    mTextMessage.setText("Home" + "\na\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n\n\n\n");
                    return true;
                case R.id.navigation_groups:
                    goToGroups();
                    return true;
                case R.id.navigation_profile:
                    goToProfile();
                    return true;
                case R.id.navigation_notifications:
                    goToNotifications();
                    return true;
            }
            return false;
        }

    };



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);
        navigation.setSelectedItemId(R.id.navigation_home);
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
