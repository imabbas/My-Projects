package com.example.aadil.bodycalculator;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button bmiButton = (Button) findViewById(R.id.btn);
        Button fatPercentage = (Button) findViewById(R.id.bodyFatBtn);

        assert bmiButton != null;
        bmiButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, BMI.class));
            }
        });

        assert fatPercentage != null;
        fatPercentage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, maleOrFemale.class));
            }
        });
    }
}
