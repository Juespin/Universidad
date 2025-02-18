% Diseño de filtro pasa bajas Chebyshev de tercer orden
% Especificaciones:
% - Atenuación máxima en banda pasante: 2 dB
% - Ganancia de voltaje (Av): 0.5
% - Frecuencia de corte (fc): 7 kHz

% Definición de parámetros
N = 3;               % Orden del filtro
Amax = 2;            % Atenuación máxima en banda pasante (dB)
fc = 7000;           % Frecuencia de corte (Hz)
Wp = 2 * pi * fc;    % Frecuencia de corte en radianes/segundo

% Diseño del filtro Chebyshev
[B, A] = cheby1(N, Amax, Wp, 's');

% Escalar los coeficientes para obtener ganancia de 0.5
B_scaled = B * 0.5;

% Suponer valores de resistencias comerciales
R1 = 10e3;   % 10 kΩ
R2 = 12e3;   % 12 kΩ
R3 = 15e3;   % 15 kΩ
h = tf(B_scaled, A)

% Obtener coeficientes normalizados del filtro escalado
k = B_scaled(4) / A(4);
wn3 = A(4);
alfa2 = A(3);
alfa1 = A(2);

% Resolver sistema de ecuaciones simbólicas para encontrar capacitores
syms C1 C2 C3

% Definir las ecuaciones
eqn1 = 1/(C1*R1) + 1/(C1*R2) + (1-k)/(R2*C2) == alfa2;
eqn2 = 1/(R1*R2*C1*C2) + 1/(R2*R3*C2*C3) == alfa1;
eqn3 = 1/(R1*R2*R3*C1*C2*C3) == wn3;

% Resolver el sistema de ecuaciones
sol = solve([eqn1, eqn2, eqn3], [C1, C2, C3]);

% Convertir resultados simbólicos a valores numéricos
C1_val = abs(double(sol.C1(1)));
C2_val = abs(double(sol.C2(1)));
C3_val = abs(double(sol.C3(1)));

% Mostrar resultados de los capacitores
fprintf('Valores de capacitores:\n');
fprintf('C1 = %.2e F\n', C1_val);
fprintf('C2 = %.2e F\n', C2_val);
fprintf('C3 = %.2e F\n', C3_val);

% Verificar ganancia
sys = tf(B_scaled, A);
dc_gain = dcgain(sys);

fprintf('Ganancia de voltaje DC: %.4f\n', abs(dc_gain));

% Graficar la respuesta de Bode
figure;
bode(sys);
title('Respuesta de Magnitud del Filtro');