package com.example.aadil.bodycalculator;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class femaleActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_female);

        Button calcbtn = (Button) findViewById(R.id.fcalcBtn);
        Button menubtn = (Button) findViewById(R.id.fmenu);

        assert calcbtn != null;
        calcbtn.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                EditText e1 = (EditText)findViewById(R.id.femaleWeight);
                assert e1 != null;
                EditText e2 = (EditText)findViewById(R.id.femaleWrist);
                assert e2 != null;
                EditText e3 = (EditText)findViewById(R.id.femaleWaist);
                assert e3 != null;
                EditText e4 = (EditText)findViewById(R.id.femaleHip);
                assert e4 != null;
                EditText e5 = (EditText)findViewById(R.id.femaleForearm);
                assert e5 != null;
                TextView t1 = (TextView)findViewById(R.id.femalePercentage);
                assert t1 != null;
                double weight = Integer.parseInt(e1.getText().toString());
                double wrist = Integer.parseInt(e2.getText().toString());
                double waist = Integer.parseInt(e3.getText().toString());
                double hip = Integer.parseInt(e4.getText().toString());
                double forearm = Integer.parseInt(e5.getText().toString());

                t1.setText(Double.toString(femaleFat(weight, wrist, waist, hip, forearm)) + "%");
//                startActivity(new Intent(BMI.this,BMI_Display.class ));
            }
        });

        assert menubtn != null;
        menubtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(femaleActivity.this, MainActivity.class));
            }
        });





    }

    public static double femaleFat(double bodyWeight, double yourWrist, double yourWaist, double yourHip, double yourForearm) {

        double bodyweight2;
        bodyweight2 = (bodyWeight * 0.732) + 8.987;

        yourWrist = yourWrist/3.14;
        yourWaist = yourWaist * 0.157;
        yourHip = yourHip * 0.249;
        yourForearm = yourForearm * 0.434;

        double x = bodyweight2 + yourWrist;
        double y = x - yourWaist;
        double z = y - yourHip;
        double leanBodyMass = yourForearm + z;
        double bodyFatPercentage = ((bodyWeight-leanBodyMass)*100)/bodyWeight;

        BigDecimal bd = new BigDecimal(bodyFatPercentage);
        bd = bd.setScale(1, RoundingMode.HALF_UP);
        bodyFatPercentage = bd.doubleValue();

        return bodyFatPercentage;

    }
}
