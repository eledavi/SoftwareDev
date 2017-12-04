package com.example2.myapplication;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
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

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
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

    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);

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
