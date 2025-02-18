
% Obtener el tamaño de la pantalla
screenSize = get(0, 'ScreenSize');

% Definir el tamaño de la figura
figWidth = 800;
figHeight = 600;

% Calcular la posición de la figura para que se abra centrada en la pantalla
figPosition = [(screenSize(3) - figWidth)/2, (screenSize(4) - figHeight)/2, figWidth, figHeight];

% Crear una interfaz gráfica para la simulación de mapeos
h.fig = figure('Name','Simulación de Mapeos','NumberTitle','off','Position',figPosition);

% Solicitar el dominio
uicontrol('Style','text','Position',[20,550,200,20],'String','Introduce la función del dominio:');
h.edit1 = uicontrol('Style','edit','Position',[20,530,200,20]);

% Solicitar la función que mapea el dominio
uicontrol('Style','text','Position',[20,500,200,20],'String','Introduce la función de mapeo:');
h.edit2 = uicontrol('Style','edit','Position',[20,480,200,20]);

% Botón para ejecutar la simulación
uicontrol('Style','pushbutton','Position',[20,400,200,20],'String','Ejecutar Simulación','Callback',@simulateMapping);

% Almacenar las manijas en la figura
guidata(h.fig, h);

% Función de Callback
function simulateMapping(hObject, eventdata)
    % Recuperar las manijas desde la figura
    h = guidata(hObject);
    
    y=sym("y");
    % Obtener el dominio, la función de mapeo y el intervalo de visualización de los campos de entrada
    y = str2sym(get(h.edit1,'String'));
    mappingFunction = str2sym(get(h.edit2,'String'));

    x = sym("x", "real");
    z = x + 1i*y;

    y = subs(y, "x", x);
    mappingFunction = subs(mappingFunction, "z", z);

    u = sym("u");
    v = sym("v");

    x_in_u = solve(u==real(mappingFunction), x);
    v = subs(imag(mappingFunction), "x", x_in_u);

    % Crear una nueva figura para mostrar las gráficas
    figure;

    % Mostrar la gráfica de la función de dominio
    subplot(2,1,1);
    ezplot(y);
    title('Gráfica de la Función de Dominio');
    xlabel('x');
    ylabel('y');

    % Mostrar la gráfica de la función mapeada
    subplot(2,1,2);
    ezplot(v);
    title('Gráfica de la Función Mapeada');
    xlabel('u');
    ylabel('v');

end