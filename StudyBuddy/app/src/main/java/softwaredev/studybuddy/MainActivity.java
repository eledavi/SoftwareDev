package softwaredev.studybuddy;

import android.database.Cursor;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.MenuItem;
import android.widget.TextView;
import android.database.sqlite.*;

public class MainActivity extends AppCompatActivity {

    private TextView mTextMessage;

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            switch (item.getItemId()) {
                case R.id.navigation_home:
                    mTextMessage.setText(R.string.title_home);
                    return true;
                case R.id.navigation_dashboard:
                    mTextMessage.setText(R.string.title_dashboard);
                    return true;
                case R.id.navigation_notifications:
                    mTextMessage.setText(R.string.title_notifications);
                    return true;
            }
            return false;
        }

    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        try {

            SQLiteDatabase studyBuddyDB = this.openOrCreateDatabase("Users", MODE_PRIVATE, null);

            studyBuddyDB.execSQL("CREATE TABLE IF NOT EXISTS userProfile (userID INT(8), email VARCHAR, firstName VARCHAR, lastName VARCHAR, university VARCHAR, major VARCHAR)");
            studyBuddyDB.execSQL("CREATE TABLE IF NOT EXISTS group (groupID INT(8), ownerID INT(8), groupName VARCHAR, courseName VARCHAR, courseID VARCHAR)");


            //studyBuddyDB.execSQL("INSERT INTO userProfile (userID, email, firstName, lastName, university, major) VALUES (80000001, 'card@nmsu.edu', 'Caitlin', 'Ard', 'New Mexico State University', 'Computer Science')");
            //studyBuddyDB.execSQL("INSERT INTO userProfile (userID, email, firstName, lastName, university, major) VALUES (80000002, 'ryansemail@nmsu.edu', 'Ryan', 'Adams', 'New Mexico State University', 'Computer Science')");
            //studyBuddyDB.execSQL("INSERT INTO userProfile (userID, email, firstName, lastName, university, major) VALUES (80000003, 'elenasemail@nmsu.edu', 'Elena', 'Davidson', 'New Mexico State University', 'Computer Science')");
            //studyBuddyDB.execSQL("INSERT INTO userProfile (userID, email, firstName, lastName, university, major) VALUES (80000004, 'angelasemail@nmsu.edu', 'Angela', 'Kearns', 'New Mexico State University', 'Computer Science')");
            studyBuddyDB.execSQL("INSERT INTO group (groupID, ownerID, groupName, courseName, courseID) VALUES (40000001, 80000001, 'Calc Squad waddup', 'Calculus II', 'MATH 192G')");



            Cursor c = studyBuddyDB.rawQuery("SELECT * FROM userProfile", null);

            int userIDIndex = c.getColumnIndex("userID");
            int emailIndex = c.getColumnIndex("email");
            int firstNameIndex = c.getColumnIndex("firstName");
            int lastNameIndex = c.getColumnIndex("lastName");
            int universityIndex = c.getColumnIndex("university");
            int majorIndex = c.getColumnIndex("major");

            c.moveToFirst();

            while(c != null){

                Log.i("userID", c.getString(userIDIndex));
                Log.i("email", c.getString(emailIndex));
                Log.i("firstName", c.getString(firstNameIndex));
                Log.i("lastName", c.getString(lastNameIndex));
                Log.i("university", c.getString(universityIndex));
                Log.i("major", Integer.toString(c.getInt(majorIndex)));

                c.moveToNext();

            }


            Cursor d = studyBuddyDB.rawQuery("SELECT * FROM group", null);

            int groupIDIndex = d.getColumnIndex("groupID");
            int ownerIDIndex = d.getColumnIndex("ownerID");
            int groupNameIndex = d.getColumnIndex("groupName");
            int courseNameIndex = d.getColumnIndex("courseName");
            int courseIDIndex = d.getColumnIndex("courseID");

            d.moveToFirst();

            while(d != null){

                Log.i("groupID", d.getString(groupIDIndex));
                Log.i("ownerID", d.getString(ownerIDIndex));
                Log.i("groupName", d.getString(groupNameIndex));
                Log.i("courseName", d.getString(courseNameIndex));
                Log.i("courseID", d.getString(courseIDIndex));

                d.moveToNext();

            }


        }
        catch(Exception e){

            e.printStackTrace();

        }

        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);
    }

}
