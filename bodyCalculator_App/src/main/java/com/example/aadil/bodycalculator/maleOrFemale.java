package com.example.aadil.bodycalculator;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class maleOrFemale extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_male_or_female);

        Button male = (Button) findViewById(R.id.mBtn);
        Button female = (Button) findViewById(R.id.feBtn);

        assert male != null;
        male.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(maleOrFemale.this, maleActivity.class ));
            }

        });

        assert female != null;
        female.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(maleOrFemale.this, femaleActivity.class ));
            }

    });

    }
}
