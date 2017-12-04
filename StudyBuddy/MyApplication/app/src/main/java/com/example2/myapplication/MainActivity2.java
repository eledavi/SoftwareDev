package com.example2.myapplication;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;


// Main activity for profile.
public class MainActivity2 extends AppCompatActivity {

    private TextView mTextMessage;
    private String currentState;

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {

            // TODO: These should really be different fragments!
            ClearCanvas();

            switch (item.getItemId()) {
                case R.id.navigation_home:
                    mTextMessage.setText(R.string.title_home);
                    SetupHome();
                    return true;
                case R.id.navigation_groups:
                    mTextMessage.setText("Groups");
                    SetupGroups();
                    return true;
                case R.id.navigation_profile:
                    mTextMessage.setText("Profile");
                    SetupProfile();
                    return true;
                case R.id.navigation_notifications:
                    mTextMessage.setText(R.string.title_notifications);
                    SetupNotifications();
                    return true;
            }
            return false;
        }

    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main2);

        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);

        SetupProfile();

        Button createGroupButton = (Button) findViewById(R.id.createGroup);
        createGroupButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ClearCanvas();
                AddGroupView();
            }
        });

        Button cancelAddGroup = (Button) findViewById(R.id.cancelAddGroup);
        cancelAddGroup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ClearCanvas();
                SetupGroups();
            }
        });

        Button addGroup = (Button) findViewById(R.id.addGroup);
        addGroup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                AddGroup();

            }
        });
    }

    public void AddGroupView(){
        TableLayout addGroupLayout = (TableLayout) findViewById(R.id.addGroupLayout);
        addGroupLayout.setVisibility(View.VISIBLE);
    }

    public void AddGroup(){
        Map<String, String> params = new HashMap<>();

        EditText desc = (EditText) findViewById(R.id.groupDescription);
        params.put("groupDescription", desc.getText().toString());

        EditText loc = (EditText) findViewById(R.id.groupMeetLocation);
        params.put("meetLoc", loc.getText().toString());

        EditText time = (EditText) findViewById(R.id.groupMeetTime);
        params.put("meet_time", time.getText().toString());

        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);
        params.put("myLeader", prefs.getString("userId", "Wrong!"));

        JSONObject obj = new JSONObject(params);
        String url ="http://192.168.0.3:5000/api/groups";

        JsonObjectRequest request = new JsonObjectRequest(Request.Method.POST, url, obj, new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                pr("got success");
                ClearCanvas();
                SetupGroups();
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                pr("got err");
                pr(error.getMessage());
                // TODO: add a message that there was an error.
            }
        });
        RequestQueue queue = Volley.newRequestQueue(this);
        queue.add(request);
    }

    public void SetupProfile() {
        TableLayout homeLayout = (TableLayout) findViewById(R.id.homeLayout);
        homeLayout.setVisibility(View.VISIBLE);

        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);

        setText("firstName", R.id.firstNameText);
        setText("lastName", R.id.lastNameText);
        setText("university", R.id.universityText);
        setText("major", R.id.majorText);
        setText("email", R.id.emailText);

        Map<String, String> params = new HashMap<>();
        JSONObject obj = new JSONObject(params);
        String url ="http://192.168.0.3:5000/api/groups?userId=" + prefs.getString("userId", "Wrong!");

        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, obj, new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                pr("got success");
                pr(response.toString());
                try {
                    JSONArray arr = response.getJSONArray("group_list");
                    for(int i = 0; i < arr.length(); i++) {
                        JSONObject obj = (JSONObject) arr.get(i);
                        createGroup(obj.get("groupDescription").toString());
                    }
                } catch (JSONException e) {
                    pr("err");
                }
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                pr("got err");
                pr(error.getMessage());
            }
        });
        RequestQueue queue = Volley.newRequestQueue(this);
        queue.add(request);
    }

    public void SetupGroups() {
        TableLayout groupLayout = (TableLayout) findViewById(R.id.groupLayout);
        groupLayout.setVisibility(View.VISIBLE);
    }

    public void SetupHome() {
        ClearCanvas();
    }

    public void SetupNotifications() {
        ClearCanvas();
    }

    public void ClearCanvas(){
        pr("clearing canvas");
        // clear home
        TableLayout homeLayout = (TableLayout) findViewById(R.id.homeLayout);
        homeLayout.setVisibility(View.INVISIBLE);
        // clear groups
        TableLayout groupLayout = (TableLayout) findViewById(R.id.groupLayout);
        groupLayout.setVisibility(View.INVISIBLE);
        // clear add group
        TableLayout groupAddLayout = (TableLayout) findViewById(R.id.addGroupLayout);
        groupAddLayout.setVisibility(View.INVISIBLE);

        pr("Done clearing");


    }



    private void createGroup(String name){
        pr("set");
        TableLayout groupList = (TableLayout) findViewById(R.id.groupTable);
        TableRow newRow = new TableRow(this);
        TextView newText = new TextView(this);
        newText.setText(name);
        newText.setTextSize(18);
        newRow.addView(newText);
        groupList.addView(newRow);
    }

    private void setText(String name, int id) {
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);
        TextView view = (TextView) findViewById(id);
        view.setText(prefs.getString(name, "Wrong!"));
    }

    public void pr(String msg) {
        System.out.println(msg);
    }

}
